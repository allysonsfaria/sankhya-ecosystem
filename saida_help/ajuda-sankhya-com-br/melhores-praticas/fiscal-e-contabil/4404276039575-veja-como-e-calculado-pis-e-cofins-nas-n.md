---
id: "4404276039575"
titulo: "Veja como é calculado PIS e COFINS nas notas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404276039575-Veja-como-%C3%A9-calculado-PIS-e-COFINS-nas-notas"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:23:23Z"
rotulos: ["Configuração", "COFINS", "PIS", "Impostos", "#ValidadoThiagoArantes", "Vincule o grupo cadastrado no produto/serviço e configure regras de exceção.", "Cadastre alíquota de PIS e COFINS nas respectivas telas.", "Verifique se a TOP e as preferências da empresa estão configuradas para calcular PIS e COFINS.", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# Veja como é calculado PIS e COFINS nas notas

**![Imagem 1: Cadastrar a alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/16345789534359) Cadastrar a alíquota**

Nas telas **"Alíquota de PIS"** e **"Alíquota de COFINS"** (as duas telas sãos iguais, mas se faz necessário cadastrar a regra em cada um), cadastre a alíquota e suas exceções para que no momento do lançamento da nota seja feito calculo de PIS/COFINS conforme a regra.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672647931543)

Usando o exemplo da Alíquota de COFINS

O campo **"Grupo"** é o campo principal, pois através do grupo criado aqui vai ser vinculado no cadastro de produto o grupo que vai ser usado para cálculo naquele produto.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672672660503)

O campo Grupo está ligado diretamente ao [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), assim, podemos ter um grupo chamado **"Monofásico"** e associá-lo ao cadastro de vários produtos. Sendo assim, todos os produtos que tiverem o grupo **"Monofásico"** estarão nessa exceção.

Esse mesmo grupo **"Monofásico"** pode ter outras regras de PIS e COFINS cadastradas, podendo variar ou combinar os outros campos de exceções.

**Exemplo:** Quero que no lançamento do Produto X seja considerado o Grupo '' **Monofásico**'' mas só quando for na **empresa 1.**No cadastro de alíquota deverá ter uma regra com grupo **"Monofásico",** e no campo Empresa informado **Empresa 1**

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672672662039)

**Nota:** A prioridade para determinação de alíquota será: TOP, Parceiro e Empresa.

Se não for encontrada nenhuma exceção, poderá ser utilizada uma configuração com valor padrão como:

Empresa 0; Parceiro 0; TOP 0; Alíquota 3,0.

**![Imagem 5: Vinculação do Grupo (do cadastro de alíquota) no cadastro de Produto OU Serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16345789537815) Vinculação do Grupo (do cadastro de alíquota) no cadastro de Produto OU Serviço.**

Tela Cadastro de Produtos, aba **"Impostos",** Campos **"Grupos PIS"** e **"Grupo COFINS",** vincule aqui o grupo cadastrado nas telas Alíquota de PIS e Alíquota de COFINS.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672647939223)

**![Imagem 7: Cadastro TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16345803034007) Cadastro TOP**

Na TOP que vai ser usada para o lançamento das notas, deve estar marcado na Aba Impostos os campos: **"Tem PIS"** e **"Tem COFINS"**.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672647942423)

**![Imagem 9: Preferências da Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16345789543063) Preferências da Empresa**

Na tela **"Empresa"** (Caminho de acesso: Comercial/Preferências), aba **"Propriedades",** os Campos **"Calcula PIS"** e **"Calcula COFINS"** devem estar marcados.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672647944855)

O PIS e o COFINS só pode ser visto na nota após a confirmação da mesma, seja entrada ou saída.

Assim que a nota for confirmada, clique no item da nota que deseja ver o cálculo, clique no botão **"Outras opções"**, selecione a opção **"Consultar/Alterar"** dados do imposto.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15672672675735)

E assim será possível ver se foi calculado ou não o PIS e o COFINS.

![Imagem 12: E assim será possível ver se foi calculado ou não o PIS e o COFINS.](https://ajuda.sankhya.com.br/hc/article_attachments/4404275919383)

No formato grade consegue-se ver detalhes dos valores.

![Imagem 13: No formato grade consegue-se ver detalhes dos valores.](https://ajuda.sankhya.com.br/hc/article_attachments/4404275954711)
