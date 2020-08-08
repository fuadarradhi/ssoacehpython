# ssoacehpython

Client SDK untuk bahasa pemograman Python

Install
```bash
pip install ssoacehpython
```

Contoh penggunaan
```python
from ssoacehpython import ssoclient

# get token dari POST
token = request.POST.get('token')

# load sso_secure.json
sso = ssoclient.SSOClient("/path/ke/sso_secure.json")
result = sso.ParseToken(token)

print(result.ID)
print(result.NIK)
print(result.NIP)
print(result.Nama)
print(result.HP)
print(result.Email)
print(result.TelegramID)
print(result.EmailAlternatif)
print(result.Avatar)
print(result.Datetime)

return JsonResponse({
    'status': 'success' if result.valid else 'error'
})
```
