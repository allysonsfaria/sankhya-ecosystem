---
id: "39382198218391"
titulo: "Como resolver quando a carga horária não aparece na aba Configurações de Ponto?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39382198218391-Como-resolver-quando-a-carga-hor%C3%A1ria-n%C3%A3o-aparece-na-aba-Configura%C3%A7%C3%B5es-de-Ponto"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:27Z"
rotulos: ["Configuração", "Atualização", "Folha", "eSocial", "Configuração Funcionários", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como resolver quando a carga horária não aparece na aba Configurações de Ponto?

Ao acessar a tela "Configuração de Funcionário" (**Pessoal > Cadastros > Funcionários**), o campo "Carga Horária" localizado na aba "Configurações de Ponto" pode estar em branco. No entanto, quando a opção "Dispensado do Ponto" está desabilitada, **o comportamento correto é que a carga horária esteja preenchida**.

A causa desse problema costuma ser uma inconsistência na aba "Histórico de Carga Horária". O cenário mais frequente ocorre quando já existe um registro antigo no histórico do colaborador, mas ele não reflete no campo principal de carga horária, deixando-o vazio.

### Identificação do problema

Para identificar se este é o problema que está afetando o funcionário, verifique os seguintes pontos:

**(1)** Abra a tela "Configuração de Funcionário" (**Pessoal > Cadastros > Funcionários**) e localize o colaborador desejado.

**(2)** Verifique se o campo **Carga Horária** está em branco na tela principal.

![Imagem 1: (2) Verifique se o campo Carga Horária está em branco na tela principal.](https://ajuda.sankhya.com.br/hc/article_attachments/40752207327127)

**(3)** Confirme se a opção **Dispensado do Ponto** está desabilitada para este funcionário.

![Imagem 2: (3) Confirme se a opção Dispensado do Ponto está desabilitada para este funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/40752207329431)

**(4)** Acesse a aba **Histórico de Carga Horária** e verifique se existe algum registro antigo cadastrado.

![Imagem 3: (4) Acesse a aba Histórico de Carga Horária e verifique se existe algum registro antigo cadastrado.](https://ajuda.sankhya.com.br/hc/article_attachments/40752207331735)

### Solução para atualizar a carga horária

Para corrigir a exibição da **"Carga Horária"**, siga o passo a passo abaixo:

**(1)** Abra a tela **"Configuração de Funcionário"** (Pessoal > Cadastros > Funcionários) e selecione o colaborador afetado.

**(2)** Clique na aba **Histórico de Carga Horária** e identifique qual jornada deveria estar ativa.

![Imagem 4: (2) Clique na aba Histórico de Carga Horária e identifique qual jornada deveria estar ativa.](https://ajuda.sankhya.com.br/hc/article_attachments/40752207331735)

**(3)** Inclua um novo registro nessa mesma aba, inserindo a carga horária correta e no campo Data de Referência, preencha com a data atual ou com a data em que a jornada deveria ter entrado em vigor.

![Imagem 5: (3) Inclua um novo registro nessa mesma aba, inserindo a carga horária correta e no campo Data de Referência, preencha…](https://ajuda.sankhya.com.br/hc/article_attachments/40752243837847)

**(4)** **Salve** o registro.

**(5)** Retorne à tela principal e verifique se o campo "Carga Horária" foi preenchido. Em seguida, confirme se a informação já aparece corretamente na aba Ponto Eletrônico.

![Imagem 6: (5) Retorne à tela principal e verifique se o campo "Carga Horária" foi preenchido. Em seguida, confirme se a…](https://ajuda.sankhya.com.br/hc/article_attachments/40752243838103)

**Atenção:** Se o problema afetar mais de um colaborador, será necessário identificar todos os que estão com o campo "Carga Horária" em branco e repetir este procedimento individualmente para cada um.

### Boas práticas para evitar o problema

Para evitar que esse problema se repita, certifique-se de preencher o campo "Carga Horária" no momento da admissão. Caso haja mudança na jornada do colaborador, registre a alteração na aba "Histórico de Carga Horária", informando a data correspondente. Essa prática mantém o sistema atualizado e garante a precisão das informações tanto no cadastro principal quanto nas integrações com o eSocial.

Além disso, antes de enviar eventos ao eSocial — como o **S-2200** (Cadastramento Inicial) ou **S-2206** (Alteração de Contrato) —, verifique sempre se a carga horária está vinculada corretamente ao funcionário. Isso previne inconsistências e possíveis rejeições.
