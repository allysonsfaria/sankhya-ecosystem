---
id: "36881907516567"
titulo: "NFS-e e Reforma Tributária: Configuração e Uso do IBS/CBS via Nota Gateway"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Sistemas atendidos"
atualizado_em: "2026-10-22T13:19:40Z"
rotulos: ["Configuração", "gateway", "Reforma tributária", "IBS", "CBS", "nota gateway", "nfs-e", "Documentos Eletrônicos"]
---

# NFS-e e Reforma Tributária: Configuração e Uso do IBS/CBS via Nota Gateway

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#oque) [1. Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#cadastro-servico)    ↳ [Seção Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#secao-geral)    ↳ [Seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#secao-reforma) [2. Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#top) | [3. Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#central-vendas) [4. Regras de obrigatoriedade do IBS/CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#vigencia) [5. Estrutura do XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#xml) [6. Persistência e rastreabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#persistencia) [7. Envio do Grupo de Benefício Municipal](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#beneficio-municipal) [8. Envio do grupo de Tributação Regular no JSON](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#tributacao-regular) [9. Envio do grupo de Repasses, Reembolsos e Ressarcimentos no JSON](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#repasses-reembolsos) |
| --- | --- |

---

## O que é e para que serve

Com a **Reforma Tributária (PEC 45/2019)** e a adoção do **Padrão Nacional da NFS-e**, o Sankhya OM e sua integração com o **Nota Gateway** foram atualizados para incluir os novos campos fiscais de **IBS (Imposto sobre Bens e Serviços)** e **CBS (Contribuição sobre Bens e Serviços)**. Este artigo detalha as configurações necessárias nos cadastros de Serviço, TOP e na Central de Vendas para garantir a conformidade legal na emissão da NFS-e. O artigo não cobre a configuração do IS (Imposto Seletivo) nem a parametrização de outros documentos fiscais.

---

## 1. Cadastro de Serviço

### Seção Geral

- **Código NBS** — registra o código da **Nomenclatura Brasileira de Serviços (NBS)**. O preenchimento é obrigatório para a padronização e a comunicação com o Ambiente Nacional da NFS-e na Reforma Tributária.

### Seção Reforma Tributária

- **Código Classificação Tributária Nacional** — registra a classificação tributária do serviço. Faz parte do grupo IBS/CBS e é necessário para o cálculo e a correta aplicação dos novos tributos.

---

## 2. Tipos de Operação (TOP)

- **Código Indicador Operação** — registra o código específico da operação de serviço utilizado para fins de cálculo e escrituração do IBS/CBS.
- **Consumidor Final** — define o padrão para a operação, indicando se a destinação é para o consumidor final. As opções são **Sim** ou **Não**.

---

## 3. Central de Vendas

- **Consumidor Final** — a marcação é herdada automaticamente da TOP configurada, mas permite ajuste manual no momento da emissão da nota, definindo se a destinação é para o consumidor final.

**Emissão para Consumidor Final / Auto-prestação (omissão do bloco Cliente)**

Em cenários de consumidor final não identificado ou auto-prestação, algumas prefeituras rejeitam a emissão quando o bloco do tomador é enviado sem CPF/CNPJ válido. Para atender essas prefeituras, o Sankhya OM omite automaticamente o bloco `cliente` do JSON enviado, quando o **Parceiro informado na nota possui o mesmo CNPJ e a mesma Inscrição Municipal da Empresa Emitente (prestadora)**.

O comportamento é automático — não há parâmetro ou marcação a ser habilitada. Quando o gatilho é atendido, os dados da própria empresa **não**são enviados como tomador do serviço, conforme permitido pela prefeitura.

---

## 4. Regras de obrigatoriedade do IBS/CBS

A obrigatoriedade do envio detalhado do grupo IBS/CBS é gradual, conforme o regime tributário da empresa:

| Período | Regime tributário | Regra |
| --- | --- | --- |
| A partir de 2026 | Lucro Real, Presumido e Simples Nacional acima do sublimite. | Envio das informações de IBS/CBS na NFS-e **obrigatório**. |
| A partir de 2026 | Simples Nacional e MEI. | IBS/CBS será **ignorado** ou enviado com alíquota zerada pelo Nota Gateway. |
| A partir de 2027 | Todas as empresas. | IBS/CBS **obrigatório** para todas as empresas. |

---

## 5. Estrutura do XML

O envio dos dados fiscais para o Nota Gateway pode ser feito de forma simplificada ou completa, dependendo do detalhamento fiscal configurado:

| Tipo de envio | Dados enviados | Cálculo do imposto |
| --- | --- | --- |
| **Simplificado (padrão)** | Apenas `classificacaoTributaria` e `codigoIndicadorOperacao`. | O Nota Gateway realiza o cálculo automático do IBS/CBS. |
| **Completo (cenários especiais)** | Inclui `situacaoTributaria`, `codigoTributacaoNacional` e o grupo `ibsCbs` completo. | O Sankhya OM envia as informações detalhadas para validação. |

**ℹ️ Nota**

No envio simplificado, o Sankhya OM envia os dados preenchidos nos cadastros e o cálculo de IBS/CBS ocorre conforme o retorno da API do eNotas/Portal Nacional.

---

## 6. Persistência e rastreabilidade

O Sankhya OM armazena o retorno da NFS-e no histórico da nota e nas tabelas fiscais, garantindo a rastreabilidade dos dados e as informações de autorização. As seguintes informações são registradas:

- Protocolo
- Chave de Acesso
- URL do DANFSE
- Mensagens de erro
- Todas as informações detalhadas dos novos campos e do grupo IBS/CBS

---

## 7. Envio do Grupo de Benefício Municipal (BM) no DPS

A partir das versões **4.35b462**, **4.34b364** e **4.33b235**, o Sankhya OM passa a atender ao layout oficial do DPS (padrão nacional), permitindo o envio das informações de **Benefício Municipal**. Este grupo identifica reduções na base de cálculo do ISS — por valor ou percentual — na integração com o eNotas/Nota Gateway.

### Configuração necessária

Para utilizar esta funcionalidade, preencha o código do benefício conforme a legislação do seu município:

1. Acesse a aba [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) no [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o).
2. Preencha o campo **Número de identificação do Benefício Municipal** com o código numérico de até 14 posições.

**ℹ️ Nota**

O envio do Grupo BM no XML/JSON ocorre **apenas** se o campo **Número de identificação do Benefício Municipal** estiver preenchido.

### Regras de preenchimento e envio

O sistema define automaticamente como as informações serão enviadas ao Gateway (JSON) com base na configuração da redução de base de cálculo do ISS:

| Cenário | Como será enviado no JSON |
| --- | --- |
| **Apenas código do benefício** Sem percentual ou tipo de dedução informados | Envia apenas o `codigo`. |
| **Redução por percentual** Campo "Perc. de dedução" preenchido + Tipo "Por percentual" na aba Alíquotas de ISS | Envia o `codigo` + `percentualReducaoBaseCalculo`. |
| **Redução por valor** Campo "Perc. de dedução" vazio + Tipo diferente de "Por percentual" na aba Alíquotas de ISS | Envia o `codigo` + `valorReducaoBaseCalculo` (valor efetivamente deduzido). |

### Exemplos técnicos (JSON)

Para conferência técnica ou depuração, veja como os dados são gerados na integração:

**Exemplo 1 — Apenas código:**

```
"beneficioMunicipal": { "codigo": "32053090200007" }
```

**Exemplo 2 — Com percentual:**

```
"beneficioMunicipal": { "codigo": "32053090200007", "percentualReducaoBaseCalculo": 5.00 }
```

**Exemplo 3 — Com valor:**

```
"beneficioMunicipal": { "codigo": "32053090200007", "valorReducaoBaseCalculo": 146.00 }
```

---

## 8. Envio do grupo de Tributação Regular no JSON

Disponível a partir do **Sankhya Om 4.36** com o módulo **erpcore 5.22.0**.

Quando a alíquota de IBS/CBS utilizada na operação tem o código de classificação tributária regular preenchido, o Sankhya Om inclui o grupo `tributacaoRegular` dentro de `servico.ibsCbs` no JSON enviado ao Nota Gateway, com o código que você cadastrou. Se nenhum código estiver preenchido, o grupo não é enviado e o JSON permanece no formato anterior.

O código é obtido na seguinte ordem de precedência:

1. IBS Municipal
2. IBS Estadual, quando o IBS Municipal não estiver preenchido
3. CBS, quando o IBS Municipal e o IBS Estadual não estiverem preenchidos

**Estrutura enviada:**

```
"ibsCbs": {
  "classificacaoTributaria": "550016",
  "codigoIndicadorOperacao": "030101",
  "tributacaoRegular": {
    "classificacaoTributaria": "000001"
  }
}
```

**⚠️ Atenção**

Classificações tributárias que exigem a tributação regular, como a 550016 utilizada com a situação tributária 550, são rejeitadas pela prefeitura quando o grupo não é enviado. Preencha o código de classificação tributária regular no [cadastro da alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199#h_01KT48EXVZ4ETGVTMQK21F7Q7N) antes de emitir.

---

## 9. Envio do grupo de Repasses, Reembolsos e Ressarcimentos no JSON

Disponível a partir do **Sankhya Om 4.36** com o módulo **erpcore 5.23.6**.

Os registros da aba **Repasses e reembolsos de terceiros**, na grade **Referências e ajustes da NFS-e** da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2ANB4N0R76KBD7AQ7XN), são enviados ao Nota Gateway no grupo `reembolsoRepasseRessarcimento`, dentro de `servico.ibsCbs`, para que os valores recebidos por conta e ordem de terceiros não componham a base de cálculo do ISSQN, do IBS e da CBS.

### Quando o grupo é enviado

O Sankhya Om inclui o grupo no JSON quando todas as condições abaixo são atendidas:

- A nota tem situação tributária (CST) de IBS/CBS, ou seja, o grupo `ibsCbs` é gerado.
- A nota tem pelo menos um registro na aba **Repasses e reembolsos de terceiros**.
- A nota não é enviada no modo multisserviço, em que cada serviço vai separado no JSON (opção **Enviar itens de NFSe separados no Json** no cadastro da Cidade).

Quando alguma condição não é atendida, o grupo não é enviado e o JSON permanece no formato anterior.

### Como os campos são preenchidos

O documento de origem é sempre enviado como `docNaoFiscalOutro`, qualquer que seja o tipo do documento. As datas vão no padrão ISO-8601, em UTC: por exemplo, 01/06/2026 no horário de Brasília é enviado como `2026-06-01T03:00:00Z`.

| Campo do JSON | Origem no Sankhya Om |
| --- | --- |
| `tipo` | **Tipo de repasse** |
| `descricao` | **Descrição do reembolso ou ressarcimento**, com até 150 caracteres |
| `documento.docNaoFiscalOutro.numero` | Número da nota informada em **Documento de origem** |
| `documento.docNaoFiscalOutro.descricao` | **Descrição do reembolso ou ressarcimento**, com até 150 caracteres |
| `documento.fornecedor` | Tipo de pessoa (J ou F), nome e CPF/CNPJ, só com números, do cadastro do parceiro informado em **Fornecedor** |
| `documento.dataEmissao` | Data de negociação do documento de origem |
| `documento.dataCompetencia` | Data de entrada e saída do documento de origem; quando não estiver preenchida, a data de negociação |
| `valor` | **Valor do reembolso, repasse ou ressarcimento** |

### Validações na emissão

Antes de enviar a nota, o Sankhya Om bloqueia a emissão e exibe uma mensagem quando:

- O documento de origem de algum registro não é encontrado.
- O valor de algum registro é zero ou negativo.
- A soma dos registros ultrapassa o valor total enviado no JSON. A mensagem exibida é: "A soma dos valores de repasse/reembolso não pode ser superior ao valor total da nota fiscal."

**Estrutura enviada:**

```
"ibsCbs": {
  "classificacaoTributaria": "000001",
  "codigoIndicadorOperacao": "030101",
  "reembolsoRepasseRessarcimento": [
    {
      "tipo": "99",
      "descricao": "MULTA DE TRANSITO",
      "documento": {
        "docNaoFiscalOutro": {
          "numero": "1",
          "descricao": "MULTA DE TRANSITO"
        },
        "fornecedor": {
          "tipoPessoa": "J",
          "nome": "DETRAN MG",
          "cpfCnpj": "64566951000105"
        },
        "dataEmissao": "2026-06-01T03:00:00Z",
        "dataCompetencia": "2026-06-01T03:00:00Z"
      },
      "valor": 70.00
    }
  ]
}
```
