---
id: "41686771632791"
titulo: "Como cadastrar dependentes do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41686771632791-Como-cadastrar-dependentes-do-colaborador"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Dependentes do Colaborador"
atualizado_em: "2026-10-16T17:47:36Z"
rotulos: ["Requisições", "ID: br.com.sankhya.cadastro.funcionarios", "ID: br.com.sankhya.rh.Requisicoes", "eSocial", "Folha de Pagamento", "Inclusão de Dependente", "Configuração Funcionários", "Pensão Alimentícia", "Cadastro", "Pessoal+", "Cadastro de Dependentes", "Salário-família"]
---

# Como cadastrar dependentes do colaborador

**Módulo:** Pessoal+
**Caminho de acesso:**

- Pessoal+ > Rotinas Folha > Requisições > Inclusão de Dependente
- Pessoal+ > Cadastros > Configuração Funcionários > Aba Dependentes

**ID da Tela:**

- br.com.sankhya.cadastro.funcionarios
- br.com.sankhya.rh.Requisicoes

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O cadastro de dependentes permite registrar pessoas vinculadas ao trabalhador para utilização em processos da folha de pagamento e no envio de informações ao eSocial.

Os dependentes podem ser utilizados para:

- dedução de IRRF;
- plano de saúde;
- pensão alimentícia;
- salário-família;
- demais rotinas que utilizam informações de dependentes.

### 2. Pré-requisitos

Antes de cadastrar um dependente, verifique se:

- o colaborador já está cadastrado;
- você possui permissão para incluir ou alterar dependentes;
- os documentos e dados do dependente estão atualizados;
- quando houver pensão alimentícia, os dados do beneficiário e da decisão judicial estejam disponíveis.

### 3. Jornada de Uso

#### 3.1 Cadastro do dependente

O cadastro do dependente pode ser feito pela **Requisição de Inclusão de Dependentes** ou diretamente na tela **Configuração Funcionários**.

##### Inclusão por Requisição

Utilize essa opção quando a empresa trabalha com fluxo de aprovação.

[GIF animado: Imagem 1: Utilize essa opção quando a empresa trabalha com fluxo de aprovação.](https://ajuda.sankhya.com.br/hc/article_attachments/41689422266775)

1. Acesse a tela **Requisições** (Pessoal+ > Rotinas Folha);
2. Selecione **Inclusão de Dependente**;
3. Localize o colaborador e clique no seu card;
4. Clique em **Incluir Dependente**;
5. Preencha os dados obrigatórios do dependente;
6. Caso seja um pensionista, marque a opção **Pensionista** e informe:
   - tipo da pensão;
   - valor ou percentual;
   - parceiro responsável pelo recebimento.
7. Clique em **Adicionar Dependente**;
8. Confirme a solicitação clicando em **Fazer Requisição** e confirme.

   A requisição será encaminhada para aprovação do responsável.

   Após a aprovação, o Departamento Pessoal poderá complementar as configurações do dependente na tela **Configuração Funcionários**, incluindo eventos de desconto e demais parâmetros necessários para os cálculos da folha.

##### Inclusão direta no cadastro do colaborador

Utilize essa opção quando possuir permissão para alterar diretamente o cadastro do colaborador.

[GIF animado: Imagem 2: Utilize essa opção quando possuir permissão para alterar diretamente o cadastro do colaborador.](https://ajuda.sankhya.com.br/hc/article_attachments/41692357376791)

1. Acessea tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Informe a **Empresa**;
3. Localize o colaborador;
4. Acesse a aba **Dependentes**;
5. Clique no botão **+ Cadastrar Dependentes**;
6. Na subaba **Geral**, preencha os dados do dependente;
7. Configure as demais informações necessárias conforme a finalidade do cadastro:
   - IRRF;
   - [plano de saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Cadastro-e-V%C3%ADnculo-de-Plano-de-Sa%C3%BAde#h_01KMJR896VGGX9V81M6AGV6R1G);
   - [pensão alimentícia](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-com-Pens%C3%A3o-Aliment%C3%ADcia);
   - [salário-família](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615).
8. Salve o cadastro.

#### 3.2 Envio do evento S-2200 ou S-2205 (eSocial)

1. Acesse a tela **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar o evento ao eSocial.
   - **S-2200**: utilize quando o dependente for incluído junto com a admissão do colaborador;
   - **S-2205**: use quando o dependente for incluído após a admissão.
2. Após o envio, verifique o retorno de sucesso no sistema. Além disso, é importante acessar o Portal do eSocial e confirmar se o dependente foi efetivamente registrado por lá.

### 4. Ponto de Atenção

- Informe corretamente o CPF, quando obrigatório.
- Os dados do dependente podem impactar diretamente o cálculo da folha de pagamento.
- Alterações em dependentes podem gerar necessidade de envio do evento **S-2205** ao eSocial.
- Dependentes utilizados para IRRF, plano de saúde ou pensão alimentícia devem possuir todas as informações exigidas pela legislação.
- Em empresas que utilizam fluxo de aprovação, as alterações realizadas por requisição somente terão efeito após aprovação.

### 5. Dicas de Usabilidade

- Mantenha os dados dos dependentes sempre atualizados.
- Revise periodicamente a validade das informações utilizadas para IRRF.
- Utilize a requisição quando houver fluxo de aprovação entre gestores e Departamento Pessoal.
- Utilize o cadastro direto apenas quando possuir autorização para realizar alterações cadastrais.
- Após alterações que impactem o eSocial, acompanhe o envio dos eventos pela Central do eSocial ou pelo Audita+.

## Perguntas Frequentes (FAQ)

**1. Posso cadastrar um dependente diretamente no cadastro do colaborador?**

Sim. Usuários com permissão podem incluir dependentes diretamente na tela **Configuração Funcionários**.

**2. Quando devo utilizar a Requisição de Inclusão de Dependente?**

Quando a empresa utiliza fluxo de aprovação para alterações cadastrais.

**3. Quem aprova uma requisição de inclusão de dependente?**

Normalmente o Departamento Pessoal ou outro responsável definido no fluxo de aprovação da empresa.

**4. Alterar um dependente gera envio ao eSocial?**

Pode gerar. Alterações em informações cadastrais do dependente podem exigir o envio do evento **S-2205**, conforme as regras do eSocial.

**5. O cadastro do dependente altera automaticamente a folha?**

Não necessariamente. O impacto depende das configurações realizadas para o dependente, como IRRF, plano de saúde, pensão alimentícia e demais parâmetros utilizados nos cálculos.

**6. Posso cadastrar um dependente apenas para plano de saúde?**

Sim. O dependente pode ser utilizado somente para plano de saúde, sem participação em outras rotinas, desde que configurado dessa forma.

**7. Posso cadastrar um dependente como pensionista?**

Sim. Nesse caso é necessário informar os dados da pensão alimentícia, como tipo de pensão, valor ou percentual e o beneficiário do recebimento.

## Artigos Relacionados

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#AbaDependentes)
- [Requisições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273)
- [Cadastro de Pensão Alimentícia](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623)
- [Cadastro de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Audita+ – Auditoria de inconsistências da Folha e do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/41658641524503)
- [Relatório S-5002 (IRRF por trabalhador)](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567)
