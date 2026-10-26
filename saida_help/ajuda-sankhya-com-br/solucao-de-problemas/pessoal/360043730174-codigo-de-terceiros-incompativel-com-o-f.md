---
id: "360043730174"
titulo: "Código de Terceiros incompatível com o FPAS informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043730174-C%C3%B3digo-de-Terceiros-incompat%C3%ADvel-com-o-FPAS-informado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:27Z"
rotulos: ["#criadoRoger", "#RevisadoLorrana", "Configuração", "Impostos", "Terceiros", "Pessoal", "eSocial", "247", "Verificar e ajustar", "Código Terceiros e FPAS", "Consultar tabela de FPAS", "Erro 247", "FPAS"]
---

# Código de Terceiros incompatível com o FPAS informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16198855965463) MENSAGEM:**

Erro 247 - Código de Terceiros incompatível com o FPAS informado.
Ação Sugerida: Para classificação tributária igual a [01, 02, 03, 04], informar 0000. Nos demais casos, o valor informado no campo deverá ser compatível com o código FPAS que consta na Tabela 4 (Códigos e Alíquotas de FPAS/Terceiros).
Elemento: /eSocial/evtTabLotacao/infoLotacao/inclusao/dadosLotacao/fpasLotacao/codTercs [0000]

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16198855966743) SOLUÇÃO**:

![Imagem 3: Para correção, siga os passos abaixo de acordo com produto utilizado:](https://ajuda.sankhya.com.br/hc/article_attachments/16198840987159) Para correção, siga os passos abaixo de acordo com produto utilizado:

#### **(1)** PESSOAL + / W

Acesse Pessoal+ » Cadastros » Registro Fiscal >> aba **"Geral"** campo **"Códigos INSS Terceiros".**

Verifique o valor informado no campo INSS Terceiros, que dever ser compatível com o campo **"Cód. FPAS"**, também informado nessa tela. 

![Imagem 4: Verifique o valor informado no campo INSS Terceiros , que dever ser compatível com o campo "Cód. FPAS" , também…](https://ajuda.sankhya.com.br/hc/article_attachments/25777127357719)

#### **(1)** MGE Pessoal

Acesse MGEPessoal » Avançado » Registro Fiscal, aba **"Informações",** campo **"Códigos INSS Terceiros".**

Verifique o valor informado no campo INSS Terceiros, que dever ser compatível com o campo **"Cód. FPAS"**, também informado nessa tela. 

![Imagem 5: Verifique o valor informado no campo INSS Terceiros , que dever ser compatível com o campo "Cód. FPAS" , também…](https://ajuda.sankhya.com.br/hc/article_attachments/14466902036247)

**(2)** No Anexo I dos Leiautes do eSocial versão S-1.2 Tabela 04 - Códigos e Alíquotas de FPAS/Terceiros consta as compatibilidades entre os códigos de terceiros e FPAS;

**(2)** Para o preenchimento correto, busque orientações com Contador/Jurídico validando inclusive a classificação tributária da empresa.

![Imagem 6: Após os ajustes, gere os eventos e libere o S-1200.](https://ajuda.sankhya.com.br/hc/article_attachments/16198855972631) Após os ajustes, gere os eventos e libere o S-1200.

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16198840994711) CAUSA**:

Ocorre devido à falta de compatibilidade entre o código INSS Terceiros com o código FPAS do Registro Fiscal da Respectiva empresa do arquivo. Incidente ao tentar enviar o S-1020.
