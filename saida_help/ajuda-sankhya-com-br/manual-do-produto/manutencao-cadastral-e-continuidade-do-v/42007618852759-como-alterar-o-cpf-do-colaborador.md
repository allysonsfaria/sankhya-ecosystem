---
id: "42007618852759"
titulo: "Como alterar o CPF do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42007618852759-Como-alterar-o-CPF-do-colaborador"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Manutenção Cadastral e Continuidade do Vínculo"
atualizado_em: "2026-10-02T15:19:02Z"
rotulos: ["Eventos", "eSocial", "Configuração Funcionários", "Cadastro", "Pessoal+", "evento S-2200 - Admissão", "evento S-2299 - Desligamento", "S-2399 — Término do vínculo", "S-2300 — Novo cadastramento do trabalhador"]
---

# Como alterar o CPF do colaborador

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > Configuração Funcionários > Outras Ações > Alterar CPF
**ID da Tela:** br.com.sankhya.rh.ConfiguracaoFuncionarios

---

## Descrição e Usabilidade

A rotina **Alterar CPF** permite realizar a alteração do CPF de colaboradores que já possuem vínculo registrado no eSocial, atendendo às regras estabelecidas pelo governo para esse tipo de alteração.

Como o CPF é utilizado como identificador do trabalhador nos eventos do eSocial, a alteração não consiste apenas na atualização do cadastro. O sistema cria um novo cadastro para o colaborador com o novo CPF e mantém o cadastro anterior para preservar o histórico das informações já transmitidas ao governo.

Durante esse processo, o sistema gera automaticamente os eventos necessários para encerrar o vínculo associado ao CPF anterior e criar o novo vínculo com o CPF atualizado, conforme a categoria do trabalhador.

A alteração somente poderá ser realizada quando todas as condições abaixo forem atendidas:

- empresa ativa;
- referência da alteração aberta;
- fechamento do eSocial (S-1299) ainda não realizado para a competência;
- trabalhador em situação normal;
- envio anterior do S-2200 ou S-2300 concluído com sucesso;
- inexistência de folhas calculadas na competência da alteração;
- inexistência de eventos pendentes de envio ao eSocial;
- inexistência de eventos aguardando retorno do governo;
- inexistência de alterações posteriores à data informada para a mudança do CPF.

### Pré-requisitos

Antes de iniciar o processo, verifique se:

- o novo CPF do trabalhador consta como regular na Receita Federal;
- o colaborador está devidamente cadastrado;
- possui permissão para realizar a alteração de CPF e gerar eventos do eSocial.

### Jornada de Uso

#### **(1)** Alterar CPF

[GIF animado: Imagem 1: (1) Alterar CPF](https://ajuda.sankhya.com.br/hc/article_attachments/42009313064471)

| **⚠️** **Atenção**  A alteração de CPF somente deve ser realizada quando todos os dados do trabalhador permanecerem os mesmos, alterando-se apenas o número do CPF.  Caso existam outras alterações cadastrais ou contratuais, elas deverão ser realizadas pelas rotinas específicas após a conclusão da alteração do CPF. |
| --- |

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Localize a **Empresa** e o **Colaborador** desejado;
3. Clique no botão **Outras Opções** e, posteriomente, selecione **Alterar CPF**;
4. Informe:
   - o **Novo** **CPF**;
   - a **Data Alteração**;
   - a **Nova Matrícula** do colaborador;
   - opcionalmente, preencha o campo **Observação** para registrar informações complementares sobre a alteração do CPF.
5. Confirme a operação.

   Ao confirmar a alteração do CPF:

   - o cadastro atual do colaborador é preservado;
   - um novo cadastro é criado automaticamente com o novo CPF;
   - é gerado um novo código de funcionário;
   - poderá ser gerada uma nova matrícula, conforme a configuração da empresa;
   - o cadastro anterior passa a representar o histórico do vínculo com o CPF antigo;
   - o sistema gera automaticamente os eventos necessários para o eSocial:
     - para empregados:
       - **evento S-2299 - Desligamento**

         O evento **S-2299** é gerado com as seguintes informações:

         - **Motivo de desligamento E-Social**: **36 – Mudança de CPF**.
         - identificação do trabalhador pelo CPF anterior;
         - novo CPF informado no campo **Novo CPF**;
         - **Data de Desligamento** da aba **Afastamento** definida automaticamente como **o dia imediatamente anterior à data da alteração do CPF**.

           **Exemplo**

           Data da alteração do CPF: **28/08/2025**

           Data enviada no S-2299: **27/08/2025**

           ![Imagem 2: Data enviada no S-2299: 27/08/2025](https://ajuda.sankhya.com.br/hc/article_attachments/42009313065623)
       - **evento S-2200 - Admissão**

         Em seguida, o sistema gera o evento **S-2200**, contendo:

         - **data original de admissão**;
         - **Novo CPF**;
         - **Novo Código**;
         - **Nova Matrícula**;
         - **Tipo de Admissão**: **6 – Mudança de CPF**;

           Também é preenchido automaticamente o grupo **Mudança de CPF**, contendo:

           - CPF anterior;
           - matrícula anterior;
           - data da alteração do CPF.

             ![Imagem 3: data da alteração do CPF.](https://ajuda.sankhya.com.br/hc/article_attachments/42009352816535)
       - para trabalhadores sem vínculo empregatício (TSVE):
         - **S-2399 — Término do vínculo**;
         - **S-2300 — Novo cadastramento do trabalhador**.

#### **(1)** Descartar alteração CPF

Caso a alteração tenha sido realizada indevidamente, clique na opção **Descartar alteração CPF** e confirme a reversão.

![Imagem 4: Caso a alteração tenha sido realizada indevidamente, clique na opção Descartar alteração CPF e confirme a reversão.](https://ajuda.sankhya.com.br/hc/article_attachments/42140800908439)

A reversão somente será permitida quando:

- o novo cadastro não possuir movimentações;
- nenhum evento do eSocial tiver sido enviado com o novo CPF.

Caso existam eventos já transmitidos ao eSocial, será necessário excluí-los antes de desfazer a alteração.

### Ponto de Atenção

- A alteração de CPF deve ser realizada exclusivamente por meio da rotina **Alterar CPF**.
- O cadastro anterior é preservado para manter o histórico das informações já transmitidas ao eSocial.
- O eSocial não permite reutilizar a matrícula vinculada ao CPF anterior. Por isso, uma nova matrícula é criada para o colaborador.
- A data enviada no **S-2299** corresponde sempre ao dia imediatamente anterior à data informada para a alteração do CPF.
- O **S-2200** mantém a data original de admissão do colaborador.

## Perguntas Frequentes (FAQ)

**1. Posso alterar o CPF de qualquer colaborador?**

Não.

A rotina somente estará disponível quando todas as validações do sistema forem atendidas.

**2. Posso alterar o CPF diretamente no cadastro do colaborador?**

Não.

A alteração deve ser realizada pelo botão **Outras Opções > Alterar CPF**, pois essa rotina gera automaticamente os eventos necessários ao eSocial e preserva a consistência das informações trabalhistas e previdenciárias.

**3. O cadastro antigo é excluído?**

Não.

O sistema preserva o cadastro anterior para manter o histórico das informações já enviadas ao eSocial.

**4. A alteração gera novos eventos para o eSocial?**

Sim.

O sistema gera automaticamente os eventos necessários para encerrar o vínculo associado ao CPF anterior e criar o novo vínculo utilizando o CPF atualizado.

**5. A data de desligamento é igual à data da alteração do CPF?**

Não. O sistema envia automaticamente no evento S-2299 a data correspondente ao dia imediatamente anterior à alteração do CPF.

**6. A matrícula do colaborador permanece a mesma?**

Não. Conforme as regras do eSocial, uma nova matrícula deve ser atribuída ao colaborador após a alteração do CPF.

**7. A data de admissão é alterada?**

Não. O evento S-2200 mantém a data original de admissão do colaborador.

**8. Posso desfazer uma alteração de CPF?**

Sim, desde que o novo cadastro ainda não possua movimentações nem eventos enviados ao eSocial.
