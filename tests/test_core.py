import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from coursekit.market import quote
from coursekit.sales import load_sales, summarise
from coursekit.ai import reply, AIError

ROOT = Path(__file__).resolve().parents[1]


def test_exact_quote_and_normalisation():
    assert quote('  YaM ', 3)['total'] == '24.00'


@pytest.mark.parametrize('product,quantity', [('unknown', 1), ('yam', 0), ('yam', -1), ('yam', True), ('yam', 1.5), ('yam', 101)])
def test_reject_bad_quote(product, quantity):
    with pytest.raises(ValueError): quote(product, quantity)


def test_sample_totals_and_groups():
    df = load_sales((ROOT/'data/sales.csv').read_bytes())
    result = summarise(df, 'region')
    assert (result['rows'], result['total_units'], result['total_revenue']) == (8, 885, 11680)
    assert result['shown_groups'][0] == {'name': 'Accra', 'value': 6610.0}


@pytest.mark.parametrize('raw', [b'', b'a,b\n1,2', b'product,region,units,revenue\n',
 b'product,region,units,revenue\nyam,Accra,1',
 b'product,product,region,units,revenue\nx,x,A,1,2',
 b'product,region,units,revenue\nx,A,-1,2',
 b'product,region,units,revenue\nx,A,1.5,2',
 b'product,region,units,revenue\nx,A,1,NaN',
 b'product,region,units,revenue\nx,A,1,inf',
 b'product,region,units,revenue\n,A,1,2',b'\xff',b'x'*1_000_001])
def test_invalid_csv(raw):
    with pytest.raises(ValueError):load_sales(raw)


def test_demo_never_needs_client():
    client=Mock()
    output=reply([{'role':'user','content':'Hello'}], 'Tutor', {'APP_MODE':'demo'},client)
    assert '[DEMO - no AI request]' in output
    client.responses.create.assert_not_called()


def test_missing_live_config():
    with pytest.raises(AIError,match='needs'):
        reply([{'role':'user','content':'Hello'}], 'Tutor', {'APP_MODE':'openai','OPENAI_API_KEY':'','OPENAI_MODEL':''})


def test_api_contract_and_bounded_context():
    client=Mock(); client.responses.create.return_value=SimpleNamespace(output_text='Helpful answer',status='completed')
    history=[]
    for i in range(10):history += [{'role':'user','content':str(i)},{'role':'assistant','content':'ok'}]
    history += [{'role':'user','content':'Next'}]
    answer=reply(history,'Tutor',{'APP_MODE':'openai','OPENAI_API_KEY':'test-placeholder','OPENAI_MODEL':'test-model'},client)
    sent=client.responses.create.call_args.kwargs
    assert len(sent['input'])==11 and sent['input'][0]['role']=='user'
    assert sent['store'] is False and sent['max_output_tokens']==600
    assert answer=='Helpful answer'


@pytest.mark.parametrize('response', [SimpleNamespace(output_text='',status='completed'),SimpleNamespace(output_text='Partial',status='incomplete')])
def test_empty_or_incomplete_response(response):
    client=Mock();client.responses.create.return_value=response
    with pytest.raises(AIError):reply([{'role':'user','content':'Hi'}],'Tutor',{'APP_MODE':'openai','OPENAI_API_KEY':'test','OPENAI_MODEL':'test'},client)


def test_connection_failure_is_readable():
    import openai
    client=Mock()
    # SDK Request class follows the currently installed SDK transport library.
    request=__import__('httpx2').Request('POST','https://api.openai.com/v1/responses')
    client.responses.create.side_effect=openai.APIConnectionError(request=request)
    with pytest.raises(AIError,match='Could not reach'):
        reply([{'role':'user','content':'Hi'}],'Tutor',{'APP_MODE':'openai','OPENAI_API_KEY':'test','OPENAI_MODEL':'test'},client)


def test_assignment_unanswered_cells_do_not_crash():
    document=json.loads((ROOT/'week1/notebooks/week1-assignment.ipynb').read_text())
    namespace={}
    for cell in document['cells']:
        if cell['cell_type']=='code':exec(''.join(cell['source']),namespace)
    assert len(namespace['SCORE'])==8 and not all(namespace['SCORE'].values())


def test_real_sdk_with_mock_http_transport():
    import httpx2
    from openai import OpenAI
    seen=[]
    def handler(request):
        seen.append(json.loads(request.content))
        assert request.url.path=='/v1/responses'
        return httpx2.Response(200,json={
            'id':'resp_test','object':'response','created_at':0,'model':'test-model','status':'completed',
            'output':[{'id':'msg_test','type':'message','role':'assistant','status':'completed',
                       'content':[{'type':'output_text','text':'Verified SDK response','annotations':[]}]}]})
    with OpenAI(api_key='test-placeholder',http_client=httpx2.Client(transport=httpx2.MockTransport(handler))) as client:
        result=reply([{'role':'user','content':'Hello'}],'Tutor',
                     {'APP_MODE':'openai','OPENAI_API_KEY':'test-placeholder','OPENAI_MODEL':'test-model'},client)
    assert result=='Verified SDK response' and seen[0]['instructions']=='Tutor'


@pytest.mark.parametrize('status,expected',[(401,'Authentication'),(429,'limited'),(500,'failed')])
def test_provider_errors_do_not_leak_response_details(status,expected):
    import httpx2
    from openai import OpenAI
    def handler(request):
        return httpx2.Response(status,json={'error':{'message':'private diagnostic marker','type':'test','code':'test'}})
    with OpenAI(api_key='test-placeholder',max_retries=0,http_client=httpx2.Client(transport=httpx2.MockTransport(handler))) as client:
        with pytest.raises(AIError,match=expected) as error:
            reply([{'role':'user','content':'Hello'}],'Tutor',
                  {'APP_MODE':'openai','OPENAI_API_KEY':'test-placeholder','OPENAI_MODEL':'test-model'},client)
    assert 'private diagnostic marker' not in str(error.value)
