---
id: "42427273325079"
titulo: "Mapeamento de campos da Sankhya para a integração entre os sistemas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427273325079-Mapeamento-de-campos-da-Sankhya-para-a-integra%C3%A7%C3%A3o-entre-os-sistemas"
trilha: "PONTOTEL: Sistema de marcação de ponto > Integração entre sistemas"
atualizado_em: "2026-08-03T12:51:43Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3328da499e20b2b6a7f6a4", "sync_hash_56062c0a36c0"]
---

# Mapeamento de campos da Sankhya para a integração entre os sistemas

Este mapeamento tem por objetivo auxiliar a identificar na **Sankhya** os campos que são refletidos na **integração com a Pontotel** para auxiliar no preenchimento dos campos com os dados esperados.

As entidades estão listadas em títulos, acompanhadas do nome correspondente na Pontotel.

**Exemplo:** “Empresa (Empregador na Pontotel)”, nome na Sankhya e nome na Pontotel, respectivamente.

Para localizar uma tela com mais facilidade, no seu teclado clique nas teclas “Ctrl” + “F”, digite a entidade que procura na caixa de texto exibida e clique em “enter” para navegar entre os resultados.

---

## Empresa (Empregador na Pontotel)

Na Sankhya existem duas telas para cadastro dos dados da Empresa.

> **Caminho de acesso:** Configurações Cadastros > Empresas
>
> **Caminho de acesso:** Configurações > Cadastros > Pessoal > Empresas

## Tela Sankhya: Empresa

> **Caminho de acesso:** Configurações > Cadastros > Empresa

Dados nesta tela:

- Razão Social
- Código
- CNPJ/CPF

![Imagem 1: CNPJ/CPF](https://storage.crisp.chat/users/helpdesk/website/-/b/f/2/5/bf253d5891ce7800/a87e7909-907a-4338-86b8-df65bd_qjdhdx.png)

## Tela Sanhya: Empresa

> Caminho de acesso: Configurações > Cadastros > Pessoal > Empresa

Dados nesta tela:

- Situação (ativa)

![Imagem 2: Situação (ativa)](https://storage.crisp.chat/users/helpdesk/website/-/9/e/8/9/9e89a7ff2dc9c000/6cfb6688-8b95-4d54-acbf-10e6a6_1i207eu.png)

---

## Departamento e Cidade de Trabalho (Local de Trabalho na Pontotel)

**⚠️ AVISO:** Este fluxo é aplicado caso não utilize a a opção “Locais Ponto Pessoal Mais”. Caso utilize esta opção, verifique o Mapeamento de Campos seguinte.

O local de trabalho é constituído de duas informações recebidas da Sankhya: Departamento e Cidade de Trabalho, localizadas no cadastro do Funcionário.

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Cadastro do Funcionário desejado

## Departamento

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Cadastro do Funcionário desejado > Lotação

![Imagem 3: Caminho de acesso: Configurações > Cadastros> Pessoal > Configuração Funcionário > Cadastro do Funcionário desejado >…](https://storage.crisp.chat/users/helpdesk/website/-/a/d/5/9/ad59a59360040000/4778a72e-d945-4a41-8df5-3aa7f4_17zkalp.png)

## Cidade de Trabalho

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Cadastro do Funcionário desejado > Lotação

![Imagem 4: Caminho de acesso: Configurações > Cadastros> Pessoal > Configuração Funcionário > Cadastro do Funcionário desejado >…](https://storage.crisp.chat/users/helpdesk/website/-/f/5/f/0/f5f0a8b3f975d800/56cea629-6212-41cc-8dd2-a6babd_rcpr9y.png)

## Locais de Trabalho (Opção usar Locais Ponto Pessoal Mais ativada)

**⚠️ AVISO:** Este fluxo é aplicado caso possua a opção “Locais Ponto Pessoal Mais” ativada.

> **Caminho de acesso:** Pessoal+ > Configurações > Locais Ponto Pessoal Mais

![Imagem 5: Caminho de acesso: Pessoal+ > Configurações > Locais Ponto Pessoal Mais](https://storage.crisp.chat/users/helpdesk/website/-/7/0/a/0/70a069b2e416e000/36b4e60a-a724-4d4a-b03c-2afe5f_1km25n4.png)

Todos os campos com retângulo vermelho são obrigatórios.

---

## Carga Horária (Escala na Pontotel)

**Esta integração tem o fluxo Pontotel > Sankhya (cadastro na Pontotel refletido na Sankhya)!**

Por isso, este mapeamento não abordará o cadastro de uma Carga Horária, mas sim o vínculo de uma carga horária cadastrada na Sankhya em um Funcionário, que por consequência, resultará na Pontotel em uma escala vinculada a um empregado admitido.

> **Caminho de acesso:** Configuração Funcionário > Cadastro do Funcionário desejado > Histórico de Carga Horária

![Imagem 6: Caminho de acesso: Configuração Funcionário > Cadastro do Funcionário desejado > Histórico de Carga Horária](https://storage.crisp.chat/users/helpdesk/website/-/1/e/8/8/1e8810d3ac548c00/0a71ca01-0b85-4120-96b5-9335f2_11dxvex.png)

### Como cadastrar uma nova Carga Horária no Funcionário:

1. Na sessão “Histórico de Carga Horária”, clique no ícone de “+”:

   ![Imagem 7: Na sessão “Histórico de Carga Horária”, clique no ícone de “+”:](https://storage.crisp.chat/users/helpdesk/website/-/f/f/1/f/ff1fc9fc03b72000/1b74f9f2-5287-40d5-9fbb-f3114c_mm5wcz.png)
2. Na tabela exibida, assegure que os campos “Data:\*” e “Carga Horária” estejam preenchidos:

   ![Imagem 8: Na tabela exibida, assegure que os campos “Data:*” e “Carga Horária” estejam preenchidos:](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849ca2efa18b05717a37465/file-3V5hiEKcfj.png)
3. Após inserir os dados, o cliente deverá clicar no botão “salvar”:

![Imagem 9: Após inserir os dados, o cliente deverá clicar no botão “salvar”:](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849ca3d7377eb6e39be18a4/file-ZIHis150CQ.png)

---

## Empregado

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário

### Dados de cadastro I

- CPF
- Nome
- Empresa
- Código Funcionário
- Código Empresa
- Código Empregado Pontotel (Código Empresa + Código Funcionário)

![Imagem 10: Código Empregado Pontotel (Código Empresa + Código Funcionário)](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849ca6010d03f404b6ebeb0/file-IbtKrDOKk0.png)

### Sindicato (Regra de cálculo na Pontotel)

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Lotação > Dados Sindicais > Sindicato

Será considerado o Sindicato apenas se existir na Pontotel uma regra de cálculo com o mesmo código. Caso contrário, o empregado será cadastrado na “Regras-Padrão”.

![Imagem 11: Será considerado o Sindicato apenas se existir na Pontotel uma regra de cálculo com o mesmo código. Caso contrário, o…](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849ca82fa18b05717a37467/file-byWKkBaOtf.png)

### Data de admissão

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Admissão

![Imagem 12: Caminho de acesso: Configurações > Cadastros> Pessoal > Configuração Funcionário > Admissão](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849caafc755d13209d613bd/file-jmgnZZXf7C.png)

### Carga Horária (Escala na Pontotel)

Caso a Carga Horária correspondente não esteja cadastrada na Pontotel no momento da Admissão, o empregado será vinculado à “Escala Padrão”.

### Dados de Cadastro II

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Pessoal > Contato

- Email

![Imagem 13: Email](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849cb237377eb6e39be18a8/file-UNE5SBdMTg.png)

### Dados de Cadastro III

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Documentos

- PIS
- CTPS
- RG

![Imagem 14: RG](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849e1b77377eb6e39be190b/file-qKFQknGace.png)

### Dados de Cadastro IV

> **Caminho de acesso:** Configurações > Cadastros> Pessoal > Configuração Funcionário > Lotação

- Departamento
- Função

![Imagem 15: Função](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6849e1d048de421e76025a71/file-hoVXDWe3V3.png)

---

## Dispensas e Afastamentos

> **Caminho de acesso:** Pessoal+ > Rotinas Folha > Ocorrências

Dispensas e Afastamentos são cadastradas na mesma tela. A definição do que é uma dispensa ou um afastamento poderá variar por cliente. Para clientes no novo fluxo, consulte as configurações aplicadas ao cliente. Para clientes na versão LinkAPI, visite a documentação desta integração e observe o critério aplicado (qual tipo se refere a qual das entidades).

### Verificar se uma Ocorrência foi cadastrada para um funcionário

1. Na tela de Ocorrências, acesse o cadastro do Funcionário e clique em seu cadastro

   ![Imagem 16: Na tela de Ocorrências, acesse o cadastro do Funcionário e clique em seu cadastro](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b39244891a03b879b04c0/file-PCqjlfmBCq.png)
2. As ocorrências cadastradas para este funcionário serão exibidas

![Imagem 17: As ocorrências cadastradas para este funcionário serão exibidas](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b3932aabad112610a94f4/file-arhP1TCtzH.png)

Os registros poderão ser editados ou deletados na Sankhya e sua alteração irá refletir na Pontotel.

### Cadastrar uma dispensa para um funcionário

1. Na tela de Lançamento de Ocorrência, a depender do tipo de registro, um anexo poderá ser requerido.

   ![Imagem 18: Na tela de Lançamento de Ocorrência, a depender do tipo de registro, um anexo poderá ser requerido.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b3951a4028301e40566a6/file-OMjN7N6xCw.png)
2. As informações obrigatórias (vermelho) deverão ser preenchidas, além da “Data de término” (para ocorrências de dispensa ou afastamento com data fim definida) ou “Dias de Afastamento Previstos” (para ocorrências de afastamento indeterminado) deverá ser preenchido.

   ![Imagem 19: As informações obrigatórias (vermelho) deverão ser preenchidas, além da “Data de término” (para ocorrências de dispensa…](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b39668771b15b28b84491/file-sUGR8z60Qx.png)
3. O lançamento deverá ser confirmado pelo usuário.

   ![Imagem 20: O lançamento deverá ser confirmado pelo usuário.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b3975aabad112610a94f9/file-bdNlicYGzG.png)
4. A confirmação de ocorrência lançada é exibida.

![Imagem 21: A confirmação de ocorrência lançada é exibida.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b3ad14891a03b879b04cb/file-9YvoQW1KoN.png)

---

## Férias

Até ser confirmada na Sankhya, as Férias passam por três fluxos na Sankhya:

1. “Requisição de Férias”,
2. “Requisição de Funcionários”
3. “Cálculos”.

Apenas após ser criada, aprovada e confirmada o registro será refletido na Pontotel.

### Requisição de Férias

> **Caminho de acesso:** Pessoal+ > Rotinas Folha > Requisições

1. Na tela de Requisições, acesse “Férias”

   ![Imagem 22: Na tela de Requisições, acesse “Férias”](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40604891a03b879b04e1/file-MRCfVQ137E.png)
2. Após localizar o Funcionário, na Requisição de Férias o Aquisitivo deve ser preenchido com a data de férias prevista para o funcionário

A data de início e a data de retorno devem estar preenchidas para que o registro seja apto a integrar.

![Imagem 23: A data de início e a data de retorno devem estar preenchidas para que o registro seja apto a integrar.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40887d1f2416ee333df4/file-hQNsF6nNsk.png)

### Requisição de Funcionários

Após o registro ser lançado na tela de requisição de férias será possível aprová-lo na tela de requisição de funcionários.

> **Caminho de acesso:** Pessoal > Rotinas > Requisições Funcionários

O registro deverá ser aprovado nesta tela.

![Imagem 24: O registro deverá ser aprovado nesta tela.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b409faabad112610a9521/file-hxTdecR28C.png)

### Cálculos

> **Caminho de acesso:** Pessoal+ > Rotinas Folha > Cálculos

1. Após identificar o Funcionário, na tela “Recibo de Férias”, clique em “Confirmar Folha”

   ![Imagem 25: Após identificar o Funcionário, na tela “Recibo de Férias”, clique em “Confirmar Folha”](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40c77d1f2416ee333df5/file-qyZKDG3ab0.png)
2. Clique em “Sim” para confirmar a folha

   ![Imagem 26: Clique em “Sim” para confirmar a folha](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40d5a4028301e40566cd/file-fk7GLdIane.png)
3. Clique no ícone “V” para marcar a folha como “Conferida”

   ![Imagem 27: Clique no ícone “V” para marcar a folha como “Conferida”](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40e22943e82ed88ae0e1/file-CZiezqvOcx.png)
4. Confirme a ação no modal com clique em “Sim”

   ![Imagem 28: Confirme a ação no modal com clique em “Sim”](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b40efa4028301e40566ce/file-CvjyNTLO04.png)
5. Será exibida uma mensagem de sucesso

Apenas registros marcados como “Conferidos” e com dados obrigatórios preenchidos são aptos a integrar.

![Imagem 29: Apenas registros marcados como “Conferidos” e com dados obrigatórios preenchidos são aptos a integrar.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b410a4891a03b879b04e4/file-wTxcXuMthM.png)

---

## Usuários

Esta integração consulta a entidade Usuário na Sankhya para criar os usuários na Pontotel.

Na configuração padrão, os dados refletidos na Pontotel são originários do cadastro do usuário na Sankhya e este usuário deve estar relacionado a um Funcionário cadastrado na Sankhya.

> **Caminho de acesso:** Configurações > Controle de Acesso > Usuários

Campos na tela Usuários:

- Código do Usuário (será base para busca no log de auditorias)
- Nome do Usuário

![Imagem 30: Nome do Usuário](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b412f2943e82ed88ae0e6/file-XhxHpuCANS.png)

Página “Identificação”, na tela de Usuários:

- E-mail
- Empresa (Deve ser o mesmo que o funcionário está vinculado)
- Funcionário (Mesmo que dispensado de ponto, deve possuir um Funcionário vinculado para integrar o usuário)
- CPF (Deve ser o mesmo CPF do Funcionário)

![Imagem 31: CPF (Deve ser o mesmo CPF do Funcionário)](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/684b413c7d1f2416ee333df9/file-9j8F2s5ivg.png)
