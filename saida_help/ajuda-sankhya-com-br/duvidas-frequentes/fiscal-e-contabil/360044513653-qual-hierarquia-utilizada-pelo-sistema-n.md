---
id: "360044513653"
titulo: "Qual hierarquia utilizada pelo sistema na obtenção das contas contábeis?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513653-Qual-hierarquia-utilizada-pelo-sistema-na-obten%C3%A7%C3%A3o-das-contas-cont%C3%A1beis"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:15Z"
rotulos: ["#criadoRoger", "Configuração", "Centro de Resultado", "TOP", "Contabilização", "Financeiro", "Natureza", "Contabilização: conta contábil constante ou variável.", "Hierarquia para variáveis: natureza da receita rateio empresa.", "Erros ocorrem se a conta não for encontrada."]
---

# Qual hierarquia utilizada pelo sistema na obtenção das contas contábeis?

**(1)** Nas configurações para contabilização podemos definir o   **Tipo de Conta Contábil**   como   **Constante**   ou   **Variável**   , sendo que para cada uma destas opções, o sistema mantém o seguinte comportamento:

(2)** Constante:**

Sempre que esta   **TOP Contabilização**   for utilizada, a Conta Contábil informada no campo **"Conta Contábil"** será utilizada.

(2)** Variável:**

Escolhendo-se esta opção, o campo   Conta Contábil  apresentará as seguintes alternativas para a Contabilização referente à Conta Contábil:

![Imagem 1: Escolhendo-se esta opção, o campo Conta Contábil apresentará as seguintes alternativas para a Contabilização referente…](https://ajuda.sankhya.com.br/hc/article_attachments/17006069482519)

**(1)** Dentre as opções disponíveis para configuração do campo Conta contábil quanto o ' Tipo de Conta contábil' é igual a 'Variável  **',**   vale ressaltar as regras utilizadas pelo sistema ao configurar as seguintes opções:

**(2)** **Conta 1 Da Natureza:**

O sistema buscará a conta contábil conforme o cadastro de 'Natureza de Receita e Despesa' o conteúdo campo Conta Contábil.

O parâmetro "**CTBZNATCAB"** define se o sistema vai pegar a natureza do cabeçalho da nota direto, para encontrar a conta contábil ou se vai analisar as naturezas do financeiro. Ligado, ele pegará a natureza do cabeçalho da nota, desligado olhará as naturezas dos financeiros.

Se no financeiro da nota tiver **vários desdobramentos** e várias naturezas, o sistema ordena primeiro pela data de vencimento e, em segunda, pelo número do desdobramento. A natureza que ficar em primeiro lugar na ordenação será utilizada para encontrar a conta contábil.

Caso **não** encontre a Conta Contábil será apresentada a seguinte mensagem de erro:

'  **A Natureza Código: 'X.X.X.X.X' está sem conta contábil 1**  '.

**(2)** **Conta 2 Da Natureza:**

O sistema buscará a conta contábil conforme o cadastro de 'Natureza de Receita e Despesa', o conteúdo do campo 'Conta Contábil 2'.

O parâmetro CTBZNATCAB definirá se o sistema pegará a natureza do cabeçalho da nota direto, para encontrar a conta contábil, ou se vai analisar as naturezas do financeiro. Ligado, ele pegará a natureza do cabeçalho da nota, desligado olhará as naturezas dos financeiros.

Se estivermos contabilizando uma nota e nesta nota existir vários desdobramentos no financeiro, o sistema verifica se há rateio. Havendo, ele priorizará a natureza do rateio e no rateio existindo várias linhas será ordenado pelo percentual, do menor para o maior.

Caso não encontre a 'Conta Contábil 2' no cadastro da 'Natureza de Receita e Despesa', verifica nas configurações da contabilização o conteúdo do campo **"Tipo de Centro de Resultado**".

Sendo do tipo 'Variável' verifica o conteúdo informado no campo **"Cód. Centro de Resultado".**

Se no campo Cód. Centro de Resultado foi informado **"N-Rateio"** e ou **"Financeiro ou R-Rateio"** e a operação teve rateio, o sistema buscará no cadastro da 'Natureza de Receita e Despesa' do rateio a 'Conta Contábil 2' para se contabilizar.

Caso não encontre a 'Conta Contábil 2' em ambos os casos será apresentada a seguinte mensagem de erro:

'  **A Natureza Código: 'X.X.X.X.X' está sem Conta Contábil 2**  '

(2)** Conta do Rateio:**

O sistema buscará a conta contábil conforme o cadastro do rateio.

Caso não encontre a 'Conta contábil' e o parâmetro **"USANATXEMP"** estiver habilitado, o sistema verifica se no 'Rateio' possui 'Natureza de Receita e Despesa' informada.

Caso tenha 'Natureza de Receita e Despesa' informada, verifica no cadastro da 'Natureza de Receita e Despesa', na aba **"Empresa X Conta Contábil"**, se existe para 'Empresa' utilizada na contabilização uma 'Conta contábil' vinculada, caso exista utiliza esta 'Conta contábil' para contabilizar.

Caso **não** tenha 'Natureza de Receita e Despesa' informada no 'Rateio' ou 'Não' possua configuração na aba Empresa X Conta Contábil será apresentada a seguinte mensagem de erro:

**'O rateio Nro Único: 'YYYY' com origem 'XXXX' está sem Conta contábil.'**

Mas caso o parâmetro USANATXEMP esteja desabilitado, o sistema verifica se no 'Rateio' possui 'Natureza de Receita e Despesa' e 'Centro de Resultado' informado.

Caso tenha, o sistema verifica no cadastro da 'Natureza de Receita e Despesa' informada no 'Rateio', na aba **"CR x Contábil"** se existe o 'Centro de Resultado' do 'Rateio' vinculado a uma 'Conta contábil', caso exista o vínculo será utilizada esta 'Conta contábil' para contabilizar.

Caso não tenha 'Natureza de Receita e Despesa' e 'Centro Resultado' informados no 'Rateio' ou **Não** possua para 'Natureza de Receita e Despesa' informada no 'Rateio' configuração na aba CR x Contábil para o 'Centro de Resultado' do 'Rateio', será apresentada a seguinte mensagem de erro  :

**'O rateio Nro Único: 'YYYY' com origem 'XXXX' está sem conta contábil.'**

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17005444684183) OBSERVAÇÃO:**

Na contabilização do rateio, quando no mesmo não tenha conta informada e na sua Natureza, na aba **"CR X Conta Contábil"**, não estiver com o CR utilizado na contabilização cadastrado, o sistema busca a conta contábil da Natureza informada no cabeçalho da nota.

**(2)** **Natureza por Empresa:**

O sistema verifica no cadastro da ' Natureza de Receita e Despesa'  informada no documento, se existe configuração na aba 'Empresa x Conta Contábil' para empresa utilizada na contabilização.

Caso encontre a 'Conta Contábil' utiliza na contabilização.

Caso não encontre 'Conta contábil' será apresentada a seguinte mensagem de erro:

**'A Natureza Código: ' XXXX1 ' por Empresa Código: 'X01' está sem conta contábil.'**

**Natureza por CR**  : O sistema verifica no cadastro da ' Natureza de Receita e Despesa'  informada no documento, se existe configuração na aba 'CR x Contábil' para o 'Centro de Resultado' utilizado na contabilização.

Caso encontre a 'Conta contábil' utiliza na contabilização.

Caso não encontre a 'Conta contábil' ou NÃO possua configuração na aba 'CR x Contábil' será apresentada a seguinte mensagem de erro:

**'A Natureza Código: 'VVV3' por Centro de Resultado Código: 'CR123' está sem conta contábil.'**

Influencias do parâmetro   USANATXEMP   na rotina de contabilização  **:**

Quando   **habilitado**  :

Na tela **"Natureza de Receita e Despesa"** habilita a aba Empresa x Conta Contábil;

Na tela **"TOP Contabilização",** no campo **"Conta contábil",** quando variável habilita a opção **"Natureza por Empresa"**;

Quando   **desabilitado**  :

Na tela Natureza de Receita e Despesa habilita a aba **"C.R. x Conta Contábil"**;

Na tela TOP Contabilização, no campo Conta contábil, quando variável habilita a opção 'Natureza por CR';
