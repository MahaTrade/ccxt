# -*- coding: utf-8 -*-


def test_account(exchange, account, method):
    format = {
        'info': {},
        'code': 'BTC',
        'type': 'spot',  # 'spot', 'margin', 'futures', 'swap'
        'id': '12345',
    }
    keys = list(format.keys())
    for i in range(0, len(keys)):
        key = keys[i]
        assert key in account, exchange.id + ' ' + method + ' ' + key + ' missing from response'

    accountKeys = list(account.keys())
    assert len(keys) == len(accountKeys), exchange.id + ' ' + method + ' respone includes more keys than expected'
    assert isinstance(account['info'], dict)
    assert account['id'] is None or isinstance(account['id'], str)
    assert account['type'] is None or isinstance(account['type'], str)
    assert account['code'] is None or isinstance(account['code'], str)
