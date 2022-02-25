# django-api-cep

| METHOD | ROUTE | DESCRIPTION | 
| --- | --- | --- |
| GET | /ceps | Get all ceps |
| GET | /ceps/:cep_code | Get a cep |
| POST | /ceps | Create a cep |


## get all ceps response example: 
```
[
	{
		"id": 1,
		"cep": "01001-000",
		"logradouro": "Praça da Sé",
		"complemento": "lado ímpar",
		"bairro": "Sé",
		"localidade": "São Paulo",
		"uf": "SP",
		"ibge": "3550308",
		"gia": "1004",
		"ddd": "11",
		"siafi": "7107"
	},
	{
		"id": 2,
		"cep": "37503-130",
		"logradouro": "Rua Geraldino Campista",
		"complemento": "",
		"bairro": "Santo Antônio",
		"localidade": "",
		"uf": "MG",
		"ibge": "",
		"gia": "",
		"ddd": "",
		"siafi": ""
	},
	{
		"id": 3,
		"cep": "59141-710",
		"logradouro": "Rua Luzia Bezerra de Lima",
		"complemento": "",
		"bairro": "Rosa dos Ventos",
		"localidade": "",
		"uf": "RN",
		"ibge": "",
		"gia": "",
		"ddd": "",
		"siafi": ""
	},
	{
		"id": 4,
		"cep": "48750-000",
		"logradouro": "",
		"complemento": "",
		"bairro": "",
		"localidade": "",
		"uf": "BA",
		"ibge": "",
		"gia": "",
		"ddd": "",
		"siafi": ""
	}
]
```

## get one cep response example: 

```
[
	{
		"id": 1,
		"cep": "01001-000",
		"logradouro": "Praça da Sé",
		"complemento": "lado ímpar",
		"bairro": "Sé",
		"localidade": "São Paulo",
		"uf": "SP",
		"ibge": "3550308",
		"gia": "1004",
		"ddd": "11",
		"siafi": "7107"
	}
]
```

## body to post a new cep: 
```
{
  "cep": "48750-010"
}
```


## Libs used:
```
asgiref==3.5.0
attrs==21.4.0
backports.zoneinfo==0.2.1
bleach==4.1.0
cached-property==1.5.2
certifi==2021.10.8
charset-normalizer==2.0.12
Django==4.0.2
djangorestframework==3.13.1
drf-api-logger==1.0.10
idna==3.3
isodate==0.6.1
lxml==4.8.0
packaging==21.3
platformdirs==2.5.1
pycep-correios==5.0.0
pyparsing==3.0.7
pytz==2021.3
requests==2.27.1
requests-file==1.5.1
requests-toolbelt==0.9.1
six==1.16.0
sqlparse==0.4.2
urllib3==1.26.8
webencodings==0.5.1
zeep==4.1.0
```

## Commands to run the project: 

```
    pip install requirements.txt
```

```
    python3 manage.py runserver
```

