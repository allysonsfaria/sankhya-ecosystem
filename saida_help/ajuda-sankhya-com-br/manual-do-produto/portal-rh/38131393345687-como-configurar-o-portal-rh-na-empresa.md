---
id: "38131393345687"
titulo: "Como configurar o Portal RH na empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38131393345687-Como-configurar-o-Portal-RH-na-empresa"
trilha: "Manual do Produto > Pessoas+ > Autoatendimento: Portal RH, App e Requisições > Portal RH"
atualizado_em: "2026-10-19T21:46:46Z"
rotulos: ["Configuração", "Portal RH", "Folha de Pagamento", "Recursos Humanos", "Colaboradores"]
---

# Como configurar o Portal RH na empresa

O **Portal RH** é o ambiente onde os colaboradores acessam informações como holerite, férias, ponto, solicitações e dados cadastrais.

Para que esse acesso funcione corretamente, é necessário realizar algumas **configurações prévias na empresa da folha**.

Antes de liberar o [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433), verifique se:

- a empresa da folha está **ativa**;
- os funcionários possuem **CPF válido** e **e-mail cadastrado**;
- as integrações (quando utilizadas) estão corretamente configuradas.

**(1)** **Acesse a empresa da folha**

1. No sistema, acesse a tela **Empresa da folha de pagamento** (Pessoal+ > Cadastros).
2. Selecione a empresa que deseja configurar e vá até a **aba Portal RH**.

**(2)** **Defina as opções do Portal RH**

1. **Integra o Portal RH:** ative essa opção para que as informações da empresa e dos colaboradores sejam integradas ao **Portal RH**.
2. **Permite batida de ponto online:** ative para permitir que os funcionários registrem ponto pelo Portal RH ou aplicativo, respeitando as regras:

   1. No **Sindicato** (aba Geral), a opção **Utiliza Registro Eletrônico de Ponto Alternativo** deve estar **ativada**;
   2. Com a opção acima ativada, o sistema verifica a opção **Dispensado do Ponto** (aba Contrato da tela **Configuração Funcionários**):

      1. **Ativada:** não permite batida de ponto.
      2. **Desativada:** permite a batida.
   3. Se a opção **Bloqueia Batida de Ponto** estiver ativada (menu Contrato da tela **Configuração** **Funcionários**), o registro será bloqueado, independentemente das demais configurações.
3. **Aprovação de requisições somente pelo DP:** quando habilitada, o sistema ignora permissões do **Painel de Configurações** e considera apenas a rotina de aprovação definida na empresa.

**(3)** **Configure funcionalidades disponíveis ao colaborador**

Defina quais recursos o colaborador poderá acessar no Portal RH:

| **Campo** | **Funcionalidade** | **Observação** |
| --- | --- | --- |
| Modelo hollerit | Selecione o modelo de visualização/impressão do holerite (contracheque) pré-definido na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694). | Os **Modelo hollerit** e **Modelo Ponto** foram adicionados ao banco de dados através do botão **Atualizar relatórios da base** do [Painel de Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057070074-Como-cadastrar-uma-empresa-para-a-folha-de-pagamento#PaineldeConfigura%C3%A7%C3%B5es). Porém, é possível cadastrar um novo relatório através da tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados) e em seguida indicá-lo nesta tela, se for preciso a personalização de um modelo específico. |
| Modelo ponto | Selecione o modelo de visualização/impressão dos registros de ponto (frequência/assiduidade) configurado previamente na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694). |
| Inibe impressão/visualização/envio e-mail hollerit | Habilite, se desejar, que o colaborador não tenha acesso ao holerite.  Nesse caso, o menu de consulta do holerite não é exibido no **Portal RH**. |  |
| Inibe impressão/visualização/envio e-mail ponto | Habilite, quando não quiser liberar o extrato de ponto para o colaborador.  Nesse caso, o menu de Ponto não é exibido no **Portal RH**. |  |
| Exibe Requisição de Alteração de Carga Horária. no Portal RH / APP? | Ative para permitir o colaborador solicitar alteração de carga horária pelo **Portal RH** ou pelo **APP Sankhya Pessoas+**. |  |
| Exibe Extrato de Ponto no Portal RH? | Habilite para permitir ao colaborador visualizar e ajustar suas marcações de ponto no **Portal RH**, mesmo sem batida online. |  |
| Exibe Evolução Salarial no Portal RH? | Ative para permitir o colaborador acompanhar sua evolução salarial no**Portal RH**. |  |
| Exibe Programação de Férias no Portal RH? | Habilite para permitir que o colaborador solicite e acompanhe suas requisições de férias pelo **Portal RH**. |  |
| Bloqueia acesso ao Portal RH a partir da Data de Desligamento | Ative para que o colaborador não tenha mais acesso ao **Portal RH** após a data de desligamento. |  |

Essas opções variam conforme a versão do sistema e as permissões configuradas.

**(4)** **Salve as configurações**

Após definir todas as opções:

- Clique em **Salvar**;
- Oriente os colaboradores sobre o primeiro acesso ao [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433).

### Pontos de atenção

- O colaborador **não conseguirá acessar o Portal RH** sem CPF válido e e-mail cadastrado.
- Nem todas as funcionalidades ficam disponíveis automaticamente:

  - algumas dependem de **parâmetros do sistema**;
  - outras exigem **configuração adicional**, como férias, ponto ou integrações externas.
- Solicitações feitas no Portal RH **não alteram a folha automaticamente** quando exigem aprovação.
- Para empresas que utilizam **totem ou computadores compartilhados**, utilize a URL específica para esse tipo de acesso.
