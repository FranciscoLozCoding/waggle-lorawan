import unittest
from parse import parse_message_payload


class TestParse(unittest.TestCase):

    def test_parse_message_payload(self):
        payload_data = '{"deduplicationId":"0541a685-f775-439a-be77-98845aaf3d41","time":"2023-04-03T21:16:01.546951465+00:00","deviceInfo":{"tenantId":"52f14cd4-c6f1-4fbd-8f87-4025e1d49242","tenantName":"ChirpStack","applicationId":"5b06bc92-0510-47c1-8f24-a807f48b94a9","applicationName":"wes-application","deviceProfileId":"d0c4ec0e-51cc-4654-ab0d-b1b614dd95c5","deviceProfileName":"Wio-E5 Dev Kit for Long Range Application","deviceName":"Lozano LoRA E5 Mini","devEui":"5a3f18b97a97247d"},"devAddr":"00362614","adr":true,"fCnt":471,"fPort":8,"data":"bWhp","object":{"Text":"mhi"},"rxInfo":[{"gatewayId":"d2ce19fffec9d449","uplinkId":34327,"rssi":-21,"snr":13.0,"channel":4,"rfChain":1,"location":{},"context":"WY4Rsw==","metadata":{"region_name":"us915","region_common_name":"US915"}}],"txInfo":{"frequency":904700000,"modulation":{"lora":{"bandwidth":125000,"spreadingFactor":10,"codeRate":"CR_4_5"}}}}'
        r = parse_message_payload(payload_data)
        self.assertEqual(r["deviceInfo"]["deviceName"], "Lozano LoRA E5 Mini")


if __name__ == "__main__":
    unittest.main()