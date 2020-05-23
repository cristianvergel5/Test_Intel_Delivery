#!/usr/bin/python3
import pytest
from intelDeliveryBot import intelDelivery
import numpy as np



@pytest.fixture
def intel_delivery_bot():
    return intelDelivery()

@pytest.mark.parametrize('username,password,expected', [
    ('cristianvergel', 'cristianvergel', True),  
])

def test_cancel_delivery(intel_delivery_bot, username, password, expected):
    login_status = intel_delivery_bot.singIn(username, password)
    login_status = intel_delivery_bot.cancelDelivery()
    assert login_status == expected

