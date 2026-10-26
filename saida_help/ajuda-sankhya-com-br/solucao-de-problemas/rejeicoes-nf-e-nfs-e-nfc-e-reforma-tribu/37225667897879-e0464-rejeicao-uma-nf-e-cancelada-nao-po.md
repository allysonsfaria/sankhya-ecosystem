---
id: "37225667897879"
titulo: "E0464 Rejeição: Uma NF-e cancelada não pode ser informada para dedução/redução."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225667897879-E0464-Rejei%C3%A7%C3%A3o-Uma-NF-e-cancelada-n%C3%A3o-pode-ser-informada-para-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:46Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "NFS-e", "Erro", "NF-e ou NFS-e", "IBS (Imposto sobre Bens e Serviços)", "Alíquotas de CBS", "Alíquotas de IBS", "CBS (Contribuição sobre Bens e Serviços)", "Dedução/redução", "NF-e cancelada", "dedução ou redução de base de cálculo"]
---

# E0464 Rejeição: Uma NF-e cancelada não pode ser informada para dedução/redução.

**MENSAGEM**

E0464 Rejeição: Uma NF-e cancelada não pode ser informada para dedução/redução.

**SITUAÇÃO**

Ao tentar emitir uma **NF-e** ou **NFS-e** informando uma nota fiscal cancelada como documento de referência para **dedução ou redução de base de cálculo** do **IBS (Imposto sobre Bens e Serviços)** ou **CBS (Contribuição sobre Bens e Serviços)**, o sistema apresenta a rejeição.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que está sendo emitida e apresentando a rejeição.

**(2)** Selecione a nota e clique no botão **"NF-e"** e em seguida na opção **"Consultar a situação atual da nota"** para verificar o status da nota fiscal referenciada junto à Sefaz.

**(3)** Identifique qual nota fiscal **cancelada** está sendo informada como referência para dedução ou redução. Verifique se a nota referenciada possui o status **"NF-e Cancelada"**.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas'' (**Comercial » Rotinas » Central de Vendas).

**(4)** Remova a referência da nota fiscal cancelada na nota que está sendo emitida. Para isso:

- Acesse a grade **''Cabeçalho''**, e verifique o campo **''Chave NF-e referenciada''**.
- Remova a chave de acesso ou referência da NF-e cancelada que estava informada.
- Na grade de **''Itens''**, clique em **''Outras Opções'' (ícone com três pontos)** e selecione **''Consultar/Alterar Dados do Imposto do Item''**.
- Localize as abas **''IBS''** e/ou **''CBS''** com os campos relacionados a **dedução/redução**.
- Remova também qualquer chave de acesso ou referência da NF-e cancelada informada nesses campos.

**(5)** Caso seja necessário informar uma nota fiscal para dedução ou redução, certifique-se de que a nota referenciada esteja com o status **"NF-e Aprovada"** e **não cancelada**.

**(6)** Após realizar os ajustes necessários, clique no botão **"NF-e"** e selecione a opção **"Gerar Lote"** para reenviar a nota fiscal à Sefaz.

**CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que notas fiscais **canceladas** sejam utilizadas como documento de referência para **dedução ou redução da base de cálculo** do **IBS** ou **CBS**. Somente notas fiscais com status **"Aprovada"** e **válidas** podem ser referenciadas para esse fim, conforme as regras de validação estabelecidas pela **Lei Complementar nº 214/2025** da Reforma Tributária.
