---
id: "37224975528727"
titulo: "E0390 Rejeição: O grupo de informações de Atividade/Evento é obrigatório quando o código de tributação nacional pertencer ao item 12 da lista de serviços."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224975528727-E0390-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-Atividade-Evento-%C3%A9-obrigat%C3%B3rio-quando-o-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-nacional-pertencer-ao-item-12-da-lista-de-servi%C3%A7os"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:20Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "Grupo de informações de Atividade/Evento", "Item 12 da lista de serviços", "Código de tributação nacional"]
---

# E0390 Rejeição: O grupo de informações de Atividade/Evento é obrigatório quando o código de tributação nacional pertencer ao item 12 da lista de serviços.

**MENSAGEM**

E0390 Rejeição: O grupo de informações de Atividade/Evento é obrigatório quando o código de tributação nacional pertencer ao item 12 da lista de serviços.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** para serviços classificados no **item 12 da lista de serviços** (serviços de diversões, lazer, entretenimento e congêneres), o documento foi **rejeitado pela Sefaz** com a mensagem de erro E0390.

**SOLUÇÃO**

Para corrigir a rejeição E0390, siga os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Na aba **"Impostos"** no campo **"Tipo de Serviço"**, verifique se o serviço está vinculado ao **item 12 da lista de serviços**.

**(3)** Caso o serviço pertença ao **item 12**, certifique-se de que o campo **"Cód. Trib. Município NFS-e"** (Código de Tributação do Município) esteja preenchido corretamente com o código correspondente ao serviço no município.

**(4)** Acesse a tela **"Alíquotas de ISS"** (Contratos e Serviços » Arquivos » Cadastros » Alíquotas de ISS).

**(5)** Verifique se o **"Cód. Trib. Município"** está cadastrado para o serviço em questão.

**(6)** Na emissão da **NFS-e**, preencha obrigatoriamente o **grupo de informações de Atividade/Evento**, que inclui dados como:

- Nome do evento ou atividade
- Data e horário de realização
- Local do evento
- Outras informações específicas exigidas pelo município

**(7)** Após realizar os ajustes necessários, **reemita a NFS-e** com as informações completas.

**CAUSA**

A rejeição E0390 ocorre porque a **Sefaz exige o preenchimento obrigatório do grupo de informações de Atividade/Evento** para serviços classificados no **item 12 da lista de serviços** (diversões, lazer, entretenimento e congêneres). Quando este grupo não é informado ou está incompleto na emissão da NFS-e, o documento é rejeitado, pois **não atende às regras de validação estabelecidas** para este tipo específico de prestação de serviço.
