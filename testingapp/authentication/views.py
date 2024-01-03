import base64
import requests
from datetime import datetime, timedelta
from .models import AppAuth

INTEGRATION_KEY = "f8659e3d-41bc-4aa7-b01e-8dfa4cf0fbcc"
SECRET_KEY = "a5dcb983-cf58-4f65-b4ab-7fe3a173dca3"
AUTHORIZATION_CODE = "eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAYABwCAqgOIJgzcSAgAgDaKzyYM3EgCAJs6VoCNWaxPszkOB6u4PUcVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjIgAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjNwATmghyjMmKT4CwJHcfePz9MAAAQx8cIgzcSA.yJw02iCN3KYakJ9StKeOJJ5PLi9Q9Lggm5z29ypJiXZfaWxtQzgeU7Ry9vr5jXUQok4gkoboqT7AmiV7MsnLXGXmBVrKDSuS2mJXaomIuzOHD-eX5quDW0cnG-MAvBVZFRMvNY4OCJpyUoNvnTOvVZe7iBtahcxJXWCX4dcVHjXUJIiC8CqHkYZ_QO2syXCbhca6kOX1zoYM5apMkOzAiYIbdEVRyqR1r2OV799TBH209TYhxHzTzEwlyFyscDyXCXnT_k_Q_gwnVTjbqCvIfhs4t5eFhOd5zu0GaoQifnWb8feb5F4k2pvxO8Cg7pNKN-ZxTPYZNY103PB3wYDS7w"


def get_auth_header():
    return base64.b64encode(f"{INTEGRATION_KEY}:{SECRET_KEY}".encode()).decode("utf-8")


def docusign_access_token():
    try:
        auth_header = get_auth_header()
        token_data = {
            "code": AUTHORIZATION_CODE,
            "grant_type": "authorization_code",
        }
        headers = {
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        token_url = "https://account-d.docusign.com/oauth/token"
        response = requests.post(token_url, data=token_data, headers=headers)

        if response.status_code == 200:
            token_info = response.json()
            print(token_info)
            # token_info = {'access_token': 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwCAQb_RnQfcSAgAgIHi3-AH3EgCAJs6VoCNWaxPszkOB6u4PUcVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjIgAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjMACAt632kQfcSDcAE5oIcozJik-AsCR3H3j8_Q.Mc1ojAb23SPMNMl8eNSWwcN7qhitzFyswy_BSoX7nWaT3dKSFGeIiEnaKVRtGjAN3D-X-gt4QZFNEkcuGfkDaaTL0RFDVSMYYpSaJ_Hf9GBhLBbvhED3kItGVorSQXSCLWKqIY2icgRCH1ajuBh9xoYSBH3yCiJjbduqKvPvfSGkV9GcDk-wqTPpM6y5SJgfdKCEZolFmaPmT0O2RkAemh320PiGDl44LvtWIJakrSmLrQvgIl_IlkZfMj42M00Wx5QPgVRUnwlYP3Qtt833DCa5E3uii4wfh7GEBfiASCn-ZgZoMeyPZtKnyRpt-Yq6JzocX3ym8NZ8yiMyjFLDZg', 'token_type': 'Bearer', 'refresh_token': 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAgABwCAQb_RnQfcSAgAgMEjyjAf3EgCAJs6VoCNWaxPszkOB6u4PUcVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjIgAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjMACAt632kQfcSDcAE5oIcozJik-AsCR3H3j8_Q.dqH3EYKvJaWDUPs8eoAZ6U8Q0WNyuVl2-SHcMRB13rXqA--gbtFc6XixA4usf1W1bCZsWIOSJqvhzu19TB6IrpoPD3Qa8LRTR1qZ26PIdkNAFtOq1YY_ZJiutOElWIF0CkyaqVIR1v1UFCflj-KXkhpzU0bC04ie-MjDfp-9zXhFkKf9it_CLI5S-uuC564F0dDFAA5__QE1ywj8Ft4TyZXOD-qsGfJbBel3q1ce6FpfsWLNX_CTkOhuaFdNYGLY80xWUe5B8OQ1H39sl3v6EXWdusqKrtcdyjVdnvDX9jnhr3o4-QzhtZw_SV94kEqBZcMXaXtyAAYjZ3Y9ZbYVqg', 'expires_in': 28800, 'scope': 'signature'}
  
            AppAuth.objects.create(
                access_token=token_info["access_token"],
                refresh_token=token_info["refresh_token"]
            )
            return token_info
        else:
            raise ValueError(
                f"Failed to obtain access token. Status code: {response.status_code}"
            )

    except Exception as e:
        print(e)


def refresh_access_token():

    try:
        access_token = AppAuth.objects.filter(id=1).first()
        if (
            not access_token.access_token
            or (datetime.utcnow() + timedelta(minutes=5)) >= access_token.expires_at
        ):
            # Construct the Authorization header
            auth_header = get_auth_header()

            # Construct the request body parameters for token refresh
            token_data = {
                "refresh_token": access_token.refresh_token,
                "grant_type": "refresh_token",
            }

            # Construct the headers
            headers = {
                "Authorization": f"Basic {auth_header}",
                "Content-Type": "application/x-www-form-urlencoded",
            }

            # Make the request to refresh the access token
            token_url = "https://account-d.docusign.com/oauth/token"
            response = requests.post(token_url, data=token_data, headers=headers)

            if response.status_code == 200:
                token_info = response.json()
                access_token.access_token = token_info["access_token"]
                access_token.refresh_token = token_info["refresh_token"]
                access_token.expires_at = datetime.utcnow() + timedelta(hours=8)
                access_token.save()
                print("access token has been refreshed")
                return access_token.access_token
            else:
                raise ValueError(
                    f"Failed to refresh access token. Status code: {response.status_code}"
                )
        else:
            print("Access token has not expired yet")
            return access_token.access_token

    except Exception as e:
        raise ValueError(f"Error refreshing access token: {str(e)}")







def token_info():
   token_info={
    'access_token': 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwAAihuYJgzcSAgAAMo-pmkM3EgCAJs6VoCNWaxPszkOB6u4PUcVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjIgAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjMAAAQx8cIgzcSDcAE5oIcozJik-AsCR3H3j8_Q.imuVaZKCsPrBxwSkICEHMNGvbPPu-M-NF0McELFaT4l2f0109_it_yXliax6npCeE0O2XsmhTDTyxutrFW6zkb5M8gQ56LfpzSgnRXWmYqakqDuEkGeD7i5o4V_U1JCJe0zeqOj_hf3UDOp8yenoVm7hUAiorr2an8_pv-q9ybEkHG7pp5DjXSdDPbXr9T7-BxK-RL977ZSAA_xOkS3Im7R4y7vPcEggFHnuYnJdteJlt5RAKGyPhLABbGxuvApIWmQ3xTGG6_vFqAEq3tCMcegU1P0ufNPyfoRfv3zwyqtCdy6G6VI3p4afFicx5MFVDvw5bJeFaVULPH_dtpMgqQ', 
    'token_type': 'Bearer', 
    'refresh_token': 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAgABwAAihuYJgzcSAgAAAqAkLkj3EgCAJs6VoCNWaxPszkOB6u4PUcVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjIgAkAAAAZjg2NTllM2QtNDFiYy00YWE3LWIwMWUtOGRmYTRjZjBmYmNjMAAAQx8cIgzcSDcAE5oIcozJik-AsCR3H3j8_Q.KVixkkMFS_ElZ5zQ0J_4PLAxJ66zv27VAA6JG2h4ceW20F6nkR1hJIk9vFv4k9LTbrHn67qRdtp6PolMNaLiZOWcHqmKQ419kPO7vczHbDSFmqT5BTezM3VZE7MskvlEgqLp80ttQpxr8Saz6G-p41m3ahF1CFgl14lRTI_wW79TjMKLIyUkJeVmC4ioS3za046e3etxxwUWUyNMu20GyOamDEErVY9eGRanYJibWQx9WrW3RjLhufDX5rDpJIbI8z57CaZ_wNaubxbtjNiI9puWw5k9PEUYg8i9JdDClClcCwBqfqCpi3DA3ffkwEoXNoXrletaI3K3R7iKJnRm_g',
    'expires_in': 28800, 
    'scope': 'signature'
    }


























      