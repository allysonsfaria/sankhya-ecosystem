---
id: "37225054963735"
titulo: "E0402 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior deve ser informado quando o país do local da prestação for informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225054963735-E0402-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-da-atividade-de-evento-ocorrido-no-exterior-deve-ser-informado-quando-o-pa%C3%ADs-do-local-da-presta%C3%A7%C3%A3o-for-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:16Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Cidades", "SEFAZ", "Erro", "Declaração de Prestação de Serviços (DPS)", "Reforma Tributária (Lei Complementar nº 214/2025)", "EX - Exterior", "Atividade realizada fora do Brasil", "País do local da prestação"]
---

# E0402 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior deve ser informado quando o país do local da prestação for informado na DPS.

**MENSAGEM**

E0402 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior deve ser informado quando o país do local da prestação for informado na DPS.

**SITUAÇÃO**

Ao tentar emitir uma **Declaração de Prestação de Serviços (DPS)** para um tomador localizado no exterior, o sistema apresenta a rejeição E0402, indicando que **faltam informações obrigatórias do endereço** da atividade realizada fora do Brasil.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **tomador do serviço** que está no exterior.

**(2)** Verifique se o campo **"País"** está preenchido corretamente no cadastro do endereço do parceiro.

**(3)** Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e valide se o **nome da cidade** está cadastrado corretamente:

- Caso a prestação seja no exterior, certifique-se de que a cidade esteja vinculada ao **país correto**;
- Verifique se o **nome da cidade** está de acordo com o padrão internacional ou conforme exigido pela legislação.

**(4)** Na emissão da **DPS**, certifique-se de que o campo **"Local de Tributação"** esteja configurado como **"Exterior"**:

- Esta opção deve ser selecionada quando a **prestação de serviço e/ou o tomador** encontrar-se no exterior;
- No XML, a tag **<Tributacao>** será preenchida com o valor **"E"**.

**(5)**  Preencha o **grupo de informações de endereço da atividade** no documento fiscal, informando:

- **Endereço completo** do local onde o serviço foi prestado no exterior;
- **País** onde ocorreu a prestação do serviço;
- Demais informações exigidas pela legislação para eventos ocorridos fora do Brasil.

**(6)** Após realizar os ajustes necessários, **redigite algum item** no cabeçalho da nota fiscal para que o sistema atualize as informações.

**(7)** Gere o **lote da DPS** novamente e transmita o documento para a Sefaz.

**CAUSA**

A rejeição ocorre quando a **Declaração de Prestação de Serviços (DPS)** é emitida para um tomador localizado no exterior e o **grupo de informações de endereço da atividade** não foi preenchido corretamente. Conforme a legislação da **Reforma Tributária (Lei Complementar nº 214/2025)**, quando o **país do local da prestação** for informado na DPS, é obrigatório detalhar o **endereço completo** onde o evento ocorreu no exterior, incluindo país, cidade e demais dados do local da prestação do serviço.
