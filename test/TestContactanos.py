import pytest
import asyncio
from playwright.sync_api import sync_playwright

def test_mensaje_debe_ser_verdadero_cuando_web_message_son_iguales(page):
    page.goto("https://www.ucp.edu.ar/")
    page.click("text=Contacto")
    page.click('#wpcf7-f79-p43-o1 > form > div.col-md-6.col-md-offset-3 > div:nth-child(6) > div > div > input')
    message = page.inner_text("#wpcf7-f79-p43-o1 > form > div.col-md-6.col-md-offset-3 > div:nth-child(1) > div > span")
    assert "El campo es obligatorio." == message