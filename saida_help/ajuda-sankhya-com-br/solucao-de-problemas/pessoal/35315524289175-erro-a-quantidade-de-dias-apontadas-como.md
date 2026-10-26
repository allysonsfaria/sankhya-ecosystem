---
id: "35315524289175"
titulo: "Erro: A quantidade de dias apontadas como lotação do funcionário código xxx, na empresa x, referência xxxx-xx-xx 00:00:00.0 excede a quantidade de dias da referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35315524289175-Erro-A-quantidade-de-dias-apontadas-como-lota%C3%A7%C3%A3o-do-funcion%C3%A1rio-c%C3%B3digo-xxx-na-empresa-x-refer%C3%AAncia-xxxx-xx-xx-00-00-00-0-excede-a-quantidade-de-dias-da-refer%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:53Z"
rotulos: ["eSocial", "Gerenciador de Folhas", "Configuração Funcionários", "Liberar para eSocial", "excede a quantidade de dias da referência", "Pessoal+", "Erro", "Erro: A quantidade de dias apontadas como lotação do funcionário código xxx", "na empresa x referência xxxx-xx-xx 00:00:00.0"]
---

# Erro: A quantidade de dias apontadas como lotação do funcionário código xxx, na empresa x, referência xxxx-xx-xx 00:00:00.0 excede a quantidade de dias da referência

**MENSAGEM**

Erro: A quantidade de dias apontadas como lotação do funcionário código xxx, na empresa x, referência xxxx-xx-xx 00:00:00.0 excede a quantidade de dias da referência.

**SITUAÇÃO**

O erro ocorre ao acessar **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e clicar em **"Liberar para eSocial"**.

**SOLUÇÃO**

**(1)** Acesse a tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) e verifique a **data de admissão** do colaborador.

![Imagem 1: (1) Acesse a tela "Configuração Funcionários" (Configurações » Cadastros » Pessoal » Configuração Funcionários) e…](https://ajuda.sankhya.com.br/hc/article_attachments/35628648089751)

**(2)** Acesse a tela **"Movimentação de Tomador de Serviço"** (Pessoal+ » Rotinas Folha » Movimentação de Tomador de Serviço) e verifique a **"Data inicial da lotação"** no histórico.

![Imagem 2: (2) Acesse a tela "Movimentação de Tomador de Serviço" (Pessoal+ » Rotinas Folha » Movimentação de Tomador de Serviço)…](https://ajuda.sankhya.com.br/hc/article_attachments/35628669375127)

**(3)** Alinhe as **datas de admissão** e **alocação do tomador**, garantindo que sejam iguais ou que a data de alocação seja posterior à data de admissão.

![Imagem 3: (3) Alinhe as datas de admissão e alocação do tomador , garantindo que sejam iguais ou que a data de alocação seja…](https://ajuda.sankhya.com.br/hc/article_attachments/35628669378711)

**(4)** Após o ajuste das datas, retorne ao **"Gerenciador de Folhas"** e clique novamente em **"Liberar para eSocial"**.

![Imagem 4: (4) Após o ajuste das datas, retorne ao "Gerenciador de Folhas" e clique novamente em "Liberar para eSocial" .](https://ajuda.sankhya.com.br/hc/article_attachments/35315535367575)

**CAUSA**

O erro é causado por **divergências entre as datas** de admissão do colaborador e as datas de alocação no tomador de serviço. O sistema detecta inconsistência quando a data inicial da lotação é anterior à data de admissão do funcionário.
