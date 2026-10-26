---
id: "14449143541911"
titulo: "Não foram encontradas configurações para calculo do imposto \"CSLL’ "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14449143541911-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-calculo-do-imposto-CSLL"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-25T19:53:38Z"
rotulos: ["CORE_E04491", "Produtos", "Configuração", "Empresa", "CSLL", "Impostos", "TOP", "Falta de exceção CSLL", "Configuração CSLL ausente", "Verifique marcações e filtros"]
---

# Não foram encontradas configurações para calculo do imposto "CSLL’ 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16858993723927) MENSAGEM:**

Não foram encontradas configurações para cálculo do imposto 'CSLL’ .

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16858993724951)SOLUÇÃO:**

![Imagem 3: Verifique nos cadastros abaixo se as marcações referentes ao Cálculo de CSLL encontram-se adequadas ao seu lançamento:](https://ajuda.sankhya.com.br/hc/article_attachments/16858977581207) Verifique nos cadastros abaixo se as marcações referentes ao Cálculo de CSLL encontram-se adequadas ao seu lançamento:

- Tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), aba **"Propriedades"**: '**Calcula CSLL?**'
- Tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"Impostos":** '**Tem CSLL**'
- Tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros), aba **"Impostos"**: **'Grupo CSLL'**

![Imagem 4: Na Tela "Alíquotas de CSLL" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) realize um filtro com as…](https://ajuda.sankhya.com.br/hc/article_attachments/16858993730071) Na Tela **"Alíquotas de CSLL"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) realize um filtro com as informações referente ao seu lançamento, considerando os campos abaixo:

- Deve existir uma configuração nessa tela com o mesmo **grupo** informado no cadastro do produto, campo: **'Grupo CSLL'**, com os campos **Tipo** (Entrada/Saída) e **Empresa** correspondentes.
- Se os campos **Parceiro/TOP** encontrarem-se sem informações, significa que essa alíquota será utilizada para todos os parceiros/TOP'S referente aquele **grupo**.
- **Necessário compreender que tratando-se de nota fiscal eletrônica, mesmo que não exista incidência desse imposto, as configurações citadas acima deverão existir, mesmo que para uma alíquota = 0 (zero).**

![Imagem 5: Caso não exista o cadastro acima que atenda ao seu lançamento, realize esse com apoio do seu Contador. Em caso de…](https://ajuda.sankhya.com.br/hc/article_attachments/16858993730967) Caso não exista o cadastro acima que atenda ao seu lançamento, realize esse com apoio do seu Contador. Em caso de dúvidas pontuais, acione o Service Desk. No entanto, vale destacar que a configuração não é realizada pela equipe do Service Desk, se evidenciada essa necessidade, um consultor de sua Franquia deverá ser acionado.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16858993731863)CAUSA:**

Ocorre quando não existir uma exceção de CSLL configurada para o respectivo lançamento.
