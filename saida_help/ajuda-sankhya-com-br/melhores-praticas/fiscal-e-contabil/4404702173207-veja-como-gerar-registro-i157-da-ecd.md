---
id: "4404702173207"
titulo: "Veja como gerar Registro I157 da ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404702173207-Veja-como-gerar-Registro-I157-da-ECD"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:23:02Z"
rotulos: ["Configuração", "ECD", "Contabilidade", "Plano de Contas", "#ValidadoThiagoArantes", "Importação e Atualização: Importe o plano de contas anterior atualize contas e vincule contas analíticas novas e antigas.", "Configuração Inicial: Defina na tela \"Empresa\" se houve mudança de plano de contas.", "Vinculação de Contas: Crie e configure a vinculação de contas contábeis externas incluindo máscara do plano anterior.", "Registro I157"]
---

# Veja como gerar Registro I157 da ECD

**Registro I157: Transferência de Saldos de Plano de Contas Anterior**

Este registro deve ser utilizado para informar as transferências de saldos das contas analíticas do plano de contas anterior para as contas analíticas do plano de contas novo.

![Imagem 1: Na tela "Empresa" (Caminho de acesso: Contabilidade » Preferências » Empresa), aba "Plano de contas", campo "Indicador…](https://ajuda.sankhya.com.br/hc/article_attachments/16369399187479) Na tela **"Empresa"** (Caminho de acesso: Contabilidade » Preferências » Empresa), aba **"Plano de contas",** campo **"Indicador de mudança de plano de contas":**

0 - Não houve mudança no plano de contas
1 - Houve mudança no plano de contas

Quando definido opção 1, validador vai cobrar a geração do I157.

![Imagem 2: Quando definido opção 1, validador vai cobrar a geração do I157.](https://ajuda.sankhya.com.br/hc/article_attachments/15694778560023)

![Imagem 3: Na tela " Vinculação de Contas Contábeis Externas", crie uma linha para a empresa a ser gerado o arquivo ECD. Deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/16369430407959) Na tela **"Vinculação de Contas Contábeis Externas",** crie uma linha para a empresa a ser gerado o arquivo ECD. Deve-se informar a Data Início Mudança do Plano de Contas e a Marcação Gerar no I157 da ECD deve ser feita.

![Imagem 4: Na tela " Vinculação de Contas Contábeis Externas", crie uma linha para a empresa a ser gerado o arquivo ECD. Deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/15694812416023)

![Imagem 5: Ainda na tela " Vinculação de Contas Contábeis Externas", aba "Máscara Conta Externa" , informe a máscara usada no…](https://ajuda.sankhya.com.br/hc/article_attachments/16369430409239) Ainda na tela **"Vinculação de Contas Contábeis Externas",** aba **"Máscara Conta Externa"**, informe a máscara usada no plano de contas anterior.

**Exemplo:** O plano anterior tem a seguinte estrutura de nível  1.1.11.111, a máscara ficará como no Print abaixo.

![Imagem 6: Exemplo: O plano anterior tem a seguinte estrutura de nível 1.1.11.111, a máscara ficará como no Print abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/15694814511895)

Verifique a estrutura do registro I050 no arquivo ECD anterior para definir a máscara corretamente.

Caso no arquivo ECD anterior, se contas no registro I050 eram geradas pela conta reduzida ou até mesmo sem os pontos separando os graus, por exemplo: |I050|31122019|01|A|5**|111010001**|11101|CAIXA|

Conforme exemplo acima, a máscara a ser informada na tela de vinculação será 1 nível com 9 dígitos.

**![Imagem 7: ATENÇÃO: informe mais de 1 grau somente se no arquivo ECD anterior existir os separadores no registro I050, exemplo:…](https://ajuda.sankhya.com.br/hc/article_attachments/16369399191959) ATENÇÃO:** informe mais de 1 grau somente se no arquivo ECD anterior existir os separadores no registro I050, exemplo: |I050|31122019|01|A|5**|1.1.1.01.0001|**1.1.1.01|CAIXA|

**Observação:** Se no plano de contas anterior o cliente usava CR, deverá ser informado o mesmo código que está no arquivo da ECD do ano anterior, se for 0 deixa zero, e se vazio deixar vazio.

Se for trabalhar com CR no sankhya, informar para qual CR vai o saldo.

Temos que lembrar que a geração do I157 é para informar a mudança do plano de conta e a transferência de saldo.

![Imagem 8: Na tela " Importação do Plano de Contas com base no ECD", importe aqui o plano de contas anterior por meio de algum…](https://ajuda.sankhya.com.br/hc/article_attachments/16369399192983) Na tela **"Importação do Plano de Contas com base no ECD",** importe aqui o plano de contas anterior por meio de algum arquivo ECD de anos anteriores.

Para mais informações, acesse o artigo sobre a tela em: [Importação do Plano de Contas com base no ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MjQwNDIxMjU0NzQsInRpY2tldF9pZCI6MTEwMTE0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYyOTQ2MDk3MH0.2KQplWP_aRqXSF31-W2X9svR1YTJw1xJ0Aat_uR3YCI)

![Imagem 9: Para mais informações, acesse o artigo sobre a tela em: Importação do Plano de Contas com base no ECD](https://ajuda.sankhya.com.br/hc/article_attachments/15694827613463)

![Imagem 10: Volte à tela " Vinculação de Contas Contábeis Externas", aba "Vinculação de Contas" , clique no botão "Atualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/16369399197207) Volte à tela **"Vinculação de Contas Contábeis Externas",** aba **"Vinculação de Contas"**,  clique no botão **"Atualizar Contas"** para que o sistema traga para essa tela o plano de contas novo que existe no sistema, para a partir dele fazer as vinculações em cada uma. Aqui o sistema irá trazer somente as contas analíticas.

![Imagem 11: Volte à tela " Vinculação de Contas Contábeis Externas", aba "Vinculação de Contas" , clique no botão "Atualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/15694850874391)

No grid abaixo, faça a vinculação das contas anteriores, nas linhas das contas novas de acordo com a conta correspondente.

![Imagem 12: No grid abaixo, faça a vinculação das contas anteriores, nas linhas das contas novas de acordo com a conta…](https://ajuda.sankhya.com.br/hc/article_attachments/15694805558167)

**![Imagem 13: OBSERVAÇÃO: Na tela "Empresa" (Caminho de acesso: contabilidade » Preferências) o Registro I157 deve estar cadastrado e…](https://ajuda.sankhya.com.br/hc/article_attachments/16369399199895) OBSERVAÇÃO:** Na tela **"Empresa"** (Caminho de acesso: contabilidade » Preferências) o Registro I157 deve estar cadastrado e marcado para gerar.

![Imagem 14: OBSERVAÇÃO: Na tela "Empresa" (Caminho de acesso: contabilidade » Preferências) o Registro I157 deve estar cadastrado e…](https://ajuda.sankhya.com.br/hc/article_attachments/15694830606871)

**IMPORTANTE:** Será gerado o I157 apenas para contas com movimento que vai popular o I155.
