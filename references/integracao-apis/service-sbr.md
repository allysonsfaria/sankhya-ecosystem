# Barramento Tradicional (/mge/service.sbr)

O barramento `/mge/service.sbr` é o ponto de entrada tradicional para chamadas de serviços EJB no Sankhya OM. Suporta payloads JSON e XML.

---

## 1. Estrutura de Requisição (JSON vs. XML)

### Chamada JSON:
`POST /mge/service.sbr?serviceName=NomeServicoSP.metodo&outputType=json`
Header: `Content-Type: application/json`

```json
{
  "serviceName": "NomeServicoSP.metodo",
  "requestBody": {
    "parametro1": { "$": "valor1" },
    "parametro2": { "$": "valor2" }
  }
}
```

### Chamada XML:
`POST /mge/service.sbr?serviceName=NomeServicoSP.metodo`
Header: `Content-Type: text/xml;charset=ISO-8859-1`

```xml
<serviceRequest serviceName="NomeServicoSP.metodo">
  <requestBody>
    <parametro1>valor1</parametro1>
    <parametro2>valor2</parametro2>
  </requestBody>
</serviceRequest>
```

---

## 2. Principais Serviços Disponíveis no Barramento

| Serviço | Função |
|---|---|
| `MobileLoginSP.login` | Autenticação e obtenção do `JSESSIONID` |
| `MobileLoginSP.logout` | Encerramento da sessão no pool |
| `CRUDServiceProvider.loadRecords` | Consulta paginada em qualquer entidade do dicionário |
| `CRUDServiceProvider.saveRecord` | Inserção ou atualização de registro |
| `CRUDServiceProvider.removeRecord` | Exclusão de registro |
| `ActionButtonsSP.execute` | Execução remota de Botões de Ação Java cadastrados |
| `CACSP.incluirNota` | Criação completa de cabeçalho e itens de notas comerciais |
| `CACSP.faturarNota` | Processamento de faturamento / transformação de pedidos |

---

## 3. Invocação de Ações Customizadas (ActionButtonsSP)

Para disparar um botão de ação previamente cadastrado em uma tela via API:

```json
{
  "serviceName": "ActionButtonsSP.execute",
  "requestBody": {
    "action": {
      "actionID": "15",
      "entityName": "CabecalhoNota",
      "keys": {
        "key": [
          { "NUNOTA": { "$": "105020" } }
        ]
      }
    }
  }
}
```
