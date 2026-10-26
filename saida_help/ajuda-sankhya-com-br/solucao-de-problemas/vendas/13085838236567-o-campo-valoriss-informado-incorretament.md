---
id: "13085838236567"
titulo: "O campo valorIss informado incorretamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13085838236567-O-campo-valorIss-informado-incorretamente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-16T19:41:23Z"
rotulos: ["Configuração", "Impostos", "E186", "Prefeituras", "NFS-e", "Erro no campo valorISS", "Marque opção \"Envia ValorISS e alíquota\"", "Prefeituras calculam ISS automaticamente", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Fiscal/Contábil - KCS"]
---

# O campo valorIss informado incorretamente

**MENSAGEM**

[E186] O campo valoriss informado incorretamente

**SITUAÇÃO**

Este erro ocorre durante a emissão de NFS-e (Nota Fiscal de Serviço Eletrônica) no Padrão Nacional, ao tentar confirmar a nota fiscal. O sistema rejeita a nota informando que o **"valor do ISS"** está incorreto, mesmo quando os cálculos aparentam estar corretos na interface.

**SOLUÇÃO**

Para corrigir o erro E186, realize as configurações nas **"Preferências da Empresa"**:

**(1)** Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa).

**(2)** Navegue até a aba **"Documentos Fiscais Eletrônicos"** e acesse a sub aba **"NFS-e"**.

**(3)** Verifique a opção **"Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?"** e marque-a.

**(4)**Temos essse campo na tela "**Cidades"** (Configurações >> Cadastros >> Endereços) aba "NFS-e", realize a marcação deste campo também, pois algumas prefeituras realizam o cálculo automaticamente do ISS e exigem essa configuração.

**(5)** Caso utilize o campo **"Campos a serem convertidos conforme manual da prefeitura"**, verifique se a opção **"regime esp. tributação ISS"** está selecionada para que o sistema popule o XML adequadamente.

**(6)** Realize os ajustes necessários conforme o **"manual da prefeitura"** e as especificações da **"API"**.

**(7)** Tente emitir a nota fiscal novamente após as configurações.

**CAUSA**

O erro E186 ocorre quando o **"valor do ISS"** enviado no XML da NFS-e não corresponde ao cálculo esperado pela prefeitura. O campo **"valorIss"** deve ser calculado multiplicando a **"base de cálculo"** pela **"alíquota do ISS"**. A causa mais comum está relacionada a configurações incorretas nas preferências da empresa, onde as prefeituras que fazem o cálculo automático do ISS exigem que parâmetros específicos de envio no XML estejam ativos.

**OBSERVAÇÃO**

Caso a opção mencionada na solução não apareça na sua tela, acesse as configurações da tela e inclua o campo manualmente.
