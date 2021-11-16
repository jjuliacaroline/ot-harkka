import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        self.edulliset = Kassapaate()
        self.maukkaat = Kassapaate()
        self.maksu = Kassapaate()
        self.kortti = Maksukortti(10)

    def test_myynti_ja_kassa_tasmaa(self):
        self.assertEqual(str(self.kassa), "Kassassa on 1000 euroa")
        self.assertEqual(str(self.edulliset), "Aterioita myyty 0")
        self.assertEqual(str(self.maukkaat), "Aterioita myyty 0")

    def test_jos_edullinen_kateismaksu_riittaa(self, maksu):
        self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(str(self.kassa), "Kassassa on 10240 euroa")
        self.assertEqual(str(self.edulliset), "Edullisia aterioita myyty 1")

    def test_jos_maukas_kateismaksu_riittaa(self, maksu):
        self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(str(self.kassa), "Kassassa on 10400 euroa")
        self.assertEqual(str(self.maukkaat), "Maukkaita aterioita myyty 1")


    def test_jos_kateismaksu_ei_riita(self, maksu):
        self.assertEqual("Kassassa on 10000 euroa")
        self.assertEqual(str(self.edulliset), "Edullisia aterioita myyty 0")
        self.assertEqual(str(self.maukkaat), "Maukkaita aterioita myyty 0")
        

    def test_saldo_vahenee_oikein_jos_on_rahaa_maukkaat(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")
        self.assertEqual(str(self.maukkaat), "Maukkaita aterioita myyty 1")


    def test_saldo_vahenee_oikein_jos_on_rahaa_edullisesti(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")
        self.assertEqual(str(self.edulliset), "Edullisia aterioita myyty 1")



    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")
        

    def test_riittiko_rahat(self):
        if self.saldo_vahenee_oikein_jos_on_rahaa(self):
            return True
        else:
            return False

    
    def test_lataa_rahaa_kortille(self):
        self.kortti.lataa_rahaa(10)
        self.kassa.lataa_rahaa_kortille(10)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 20 euroa")
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 11000 euroa")
