import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa",)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.0 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_negatiivinen_summa_ei_muutTestMyCodea_saldoa(self):
        self.kortti.lataa_rahaa(-20)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_voi_syoda_edullisen_lounaan_kun_kortilla_edullisen_lounaan_hinta(self):
        self.kortti = Maksukortti(2.5)
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.0 euroa")


    def test_voi_syoda_herkkulounaan_kun_kortilla_herkkulounaan_hinta(self):
        self.kortti = Maksukortti(4)
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0 euroa")
    
    def kortin_saldo_alussa_oikein(self):
        self.kortti = 10
    
    def rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(10)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 20 euroa")

    def saldo_vahenee_oikein_jos_on_rahaa(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def riittiko_rahat(self):
        if self.saldo_vahenee_oikein_jos_on_rahaa(self):
            return True
        else:
            return False