---
id: "4403903671319"
titulo: "Como emitir uma nota de 'Transferência de crédito do ICMS/ressarcimento/restituição do ICMS-ST'?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903671319-Como-emitir-uma-nota-de-Transfer%C3%AAncia-de-cr%C3%A9dito-do-ICMS-ressarcimento-restitui%C3%A7%C3%A3o-do-ICMS-ST"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:23:33Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "ajuste", "SEFAZ", "Crédito", "ICMS", "Impostos", "CFOP", "#APOIOTHIAGOARANTES", "notadeajuste", "nota", "Transferência de Crédito", "ICMS/ressarcimento/restituição ICMS-ST", "Unidade \"Un\" valor total sem frete"]
---

# Como emitir uma nota de 'Transferência de crédito do ICMS/ressarcimento/restituição do ICMS-ST'?

**Transferência de crédito do ICMS/ressarcimento/restituição do ICMS-ST:**

| - A nota fiscal eletrônica (NF-e) também será emitida nas hipóteses de transferências de crédito acumulado de ICMS assim como nos casos de restituição do ICMS. De acordo com a legislação, há regras a serem observadas para a emissão da NF-e nessas hipóteses. - Fonte:  [Orientação de Preenchimento da NF-e - versão 2.02](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VCrU5SRXeEk=) |
| --- |

Destacam-se o preenchimento de alguns campos conforme abaixo:

- O documento abaixo cita as configurações básicas, conforme Manual de Orientação SEFAZ. Para validação do processo e configuração completa, recomendamos que seja acompanhado por um consultor de sua Unidade e validado junto ao Contador da empresa.

**Principais configurações:**

**![Imagem 1: Natureza da Operação:](https://ajuda.sankhya.com.br/hc/article_attachments/16345683199639) Natureza da Operação:**

Utilize como natureza da operação: **“Transferência de Crédito Acumulado de ICMS”** ou “**Ressarcimento de ICMS”** ou **“Restituição de ICMS/ST”,** conforme disposto na legislação Estadual;

- Tela **"Tipos de Operação-TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)
- Aba **"Livro Fiscal"**
- Campo **"Natureza da Operação (SPED)"**

**![Imagem 2: Finalidade de Emissão:](https://ajuda.sankhya.com.br/hc/article_attachments/16345679684119) Finalidade de Emissão:**

No campo **“Finalidade de emissão”** informar “NF-e de Ajuste”;

- Tela Tipos de Operação-TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)
- Aba **"NF-e/NFC-e"**
- Campo **"NF-e":** Ajuste
- Campo **"Tipo de Emissão":** Ajuste

**Ajuste:** se selecionado, indicará que a TOP será utilizada para Nota de Ajuste de Nota Fiscal Eletrônica. A opção Tipo de Emissão da aba "**Impostos"**tem que estar marcado como Ajuste;

![Imagem 3: Ajuste: se selecionado, indicará que a TOP será utilizada para Nota de Ajuste de Nota Fiscal Eletrônica. A opção Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/15083276089879)

![Imagem 4: Utilize o CST “090”;](https://ajuda.sankhya.com.br/hc/article_attachments/16345679685015) Utilize o CST “090”;

**![Imagem 5: Código e Descrição do Produto:](https://ajuda.sankhya.com.br/hc/article_attachments/16345683211159) Código e Descrição do Produto:**

4.1- Crie no sistema um produto com a **descrição** do ajuste a ser realizado: "Transferência de Crédito Acumulado de ICMS” ou “Ressarcimento de ICMS” ou “Restituição de ICMS/ST”;

4.2- O código do produto deverá ser preenchido com “CFOP5601” ou “CFOP5602” ou “CFOP5603”, conforme o caso;

- Nesse caso, utilize o campo **"Referência"** para inserir o "código do produto";
- Na aba Impostos preencha o campo **"Código produto p/NF-e"**: referência

![Imagem 6: Na aba Impostos preencha o campo "Código produto p/NF-e" : referência](https://ajuda.sankhya.com.br/hc/article_attachments/15083317693079)

![Imagem 7: Cadastre o NCM "00" com o respectivo código, na tela "Cadastro de NCM" . Logo após o cadastro, informe o código NCM…](https://ajuda.sankhya.com.br/hc/article_attachments/16345679692823) Cadastre o NCM "00" com o respectivo código, na tela **"Cadastro de NCM"**. Logo após o cadastro, informe  o código NCM como “00”;

- Tela 'Produtos' » Aba 'Geral' » Campo 'NCM'

**![Imagem 8: Origem da mercadoria – informe “0”](https://ajuda.sankhya.com.br/hc/article_attachments/16345683217431) Origem da mercadoria – informe “0”**

- Tela 'Produtos' » Aba 'Geral' » Campo 'Origem do Produto'

**![Imagem 9: Situação tributária do PIS e da COFINS: “Operação sem incidência da Contribuição”;](https://ajuda.sankhya.com.br/hc/article_attachments/16345679701015) Situação tributária do PIS e da COFINS: “Operação sem incidência da Contribuição”;**

- Tela 'Alíquotas de PIS' » Campo 'Cód. sit. tributária': 08-Sem Incidência
- Tela 'Alíquotas de COFINS' » Campo 'Cód. sit. tributária': 08-Sem Incidência

**Lançamento da nota no sistema :**

Seguem as principais informações a serem preenchidas para lançar a NF-e de Ajuste no sistema:

![Imagem 10: A 'Unidade' poderá ser preenchida com o conteúdo “Un” , quantidade: “1” e ' Valor unitário' igual ao valor da…](https://ajuda.sankhya.com.br/hc/article_attachments/16345683220887) A 'Unidade' poderá ser preenchida com o conteúdo **“Un”**, quantidade: “1” e '**Valor unitário' igual ao valor da transferência/ressarcimento/restituição.**

![Imagem 11: Valor Total Bruto dos Produtos ou Serviços – valor total da transferência/restituição/ressarcimento;](https://ajuda.sankhya.com.br/hc/article_attachments/16345679704087) Valor Total Bruto dos Produtos ou Serviços –  valor total da transferência/restituição/ressarcimento;

![Imagem 12: Modalidade do frete: indique “Sem frete”.](https://ajuda.sankhya.com.br/hc/article_attachments/16345683237399) Modalidade do frete: indique “Sem frete”.

- Central de Vendas » Rodapé » Aba 'Transporte' » Campo CIF/FOB = Sem Frete

![Imagem 13: Central de Vendas » Rodapé » Aba 'Transporte' » Campo CIF/FOB = Sem Frete](https://ajuda.sankhya.com.br/hc/article_attachments/15083406867863)
