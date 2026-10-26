# APIs REST Oficiais do Sankhya OM

As APIs REST expostas pelo Sankhya permitem operações completas de consulta e mutação de dados em formato JSON padronizado.

---

## 1. Consulta Paginada de Registros (loadRecords)

Permite consultar qualquer entidade cadastrada no Dicionário de Dados com paginação, filtros e projeção de colunas.

### Endpoint:
`POST https://seu-sankhya.com.br/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json`

### Exemplo de Payload para Busca de Parceiros:
```json
{
  "serviceName": "CRUDServiceProvider.loadRecords",
  "requestBody": {
    "dataSet": {
      "rootEntity": "Parceiro",
      "includePresentationFields": "N",
      "offsetPage": "0",
      "criteria": {
        "expression": {
          "$": "this.ATIVO = 'S' AND this.TIPPESSOA = 'J'"
        }
      },
      "entity": {
        "fieldset": {
          "list": "CODPARC,NOMEPARC,CGC_CPF,CODCID,EMAIL"
        }
      }
    }
  }
}
```

### Resposta Paginada:
```json
{
  "serviceName": "CRUDServiceProvider.loadRecords",
  "status": "1",
  "responseBody": {
    "entities": {
      "total": "1420",
      "entity": [
        {
          "f0": { "$": "100" },
          "f1": { "$": "DISTRIBUIDORA EXEMPLO S/A" },
          "f2": { "$": "12345678000199" },
          "f3": { "$": "3106200" },
          "f4": { "$": "contato@exemplo.com.br" }
        }
      ]
    }
  }
}
```

> **Atenção aos Campos:** No retorno `loadRecords`, `f0`, `f1`, `f2` correspondem à ordem informada no `fieldset.list`.

---

## 2. Inserção / Atualização de Registros (saveRecord)

### Endpoint:
`POST https://seu-sankhya.com.br/mge/service.sbr?serviceName=CRUDServiceProvider.saveRecord&outputType=json`

### Exemplo de Criação de Parceiro:
```json
{
  "serviceName": "CRUDServiceProvider.saveRecord",
  "requestBody": {
    "dataSet": {
      "rootEntity": "Parceiro",
      "dataRow": {
        "localFields": {
          "NOMEPARC": { "$": "NOVO CLIENTE INTEGRADO LTDA" },
          "TIPPESSOA": { "$": "J" },
          "CGC_CPF": { "$": "98765432000188" },
          "CODCID": { "$": "1" },
          "ATIVO": { "$": "S" }
        }
      },
      "entity": {
        "fieldset": {
          "list": "NOMEPARC,TIPPESSOA,CGC_CPF,CODCID,ATIVO"
        }
      }
    }
  }
}
```

---

## 3. Exclusão de Registro (removeRecord)

```json
{
  "serviceName": "CRUDServiceProvider.removeRecord",
  "requestBody": {
    "dataSet": {
      "rootEntity": "Parceiro",
      "criterio": {
        "expression": {
          "$": "this.CODPARC = 502"
        }
      }
    }
  }
}
```

---

## 4. Códigos de Retorno Padronizados
- `status: "1"` → Sucesso. O payload de resposta está em `responseBody`.
- `status: "0"` → Erro de negócio ou validação. Mensagem detalhada em `statusMessage`.
- `status: "3"` → Sessão expirada ou usuário não autenticado.
