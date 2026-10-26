---
id: "42632245838871"
titulo: "Como cadastrar um processo trabalhista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42632245838871-Como-cadastrar-um-processo-trabalhista"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-10-02T17:46:56Z"
rotulos: ["Processo Trabalhista", "br.com.sankhya.ProcessoTrabalhista", "Informações do Contrato de Trabalho no Processo Trabalhista", "Inclusão de Dependentes do Trabalhador no Processo Trabalhista", "Informações de Tributos Decorrentes de Processo Trabalhista"]
---

# Como cadastrar um processo trabalhista

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**Versão disponível:** A partir da 4.21
**ID da Tela:** br.com.sankhya.ProcessoTrabalhista

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A rotina **Processo Trabalhista** permite cadastrar processos trabalhistas para que as informações sejam utilizadas na geração dos eventos correspondentes do eSocial.

O cadastro reúne as informações do **declarante, processo, trabalhador e contrato de trabalho**. Após a confirmação do cadastro, o processo fica disponível para a geração do evento **S-2500 – Processo Trabalhista**.

A tela também permite cadastrar as **Informações de Tributos Decorrentes**, quando houver valores de contribuição previdenciária ou Imposto de Renda a recolher relacionados ao processo. Nesse caso, as informações são utilizadas para a geração do evento **S-2501 – Informações dos Tributos Decorrentes de Processo Trabalhista**.

### 2. Pré-requisitos

- Permissão de acesso à tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Dados do processo trabalhista, conforme a decisão judicial, ata ou acordo.
- Dados do trabalhador e, quando aplicável, dos dependentes.
- Informações do contrato de trabalho relacionadas ao processo.

### 3. Jornada de Uso

1. Acesse a tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha).
2. Selecione a **Empresa** e clique em **Pesquisar**.
3. Clique em **Adicionar Processo Trabalhista**.

   [GIF animado: Imagem 1: Clique em Adicionar Processo Trabalhista .](https://ajuda.sankhya.com.br/hc/article_attachments/42865127195927)
4. Preencha os dados do menu **Declarante**:

   [GIF animado: Imagem 2: Preencha os dados do menu Declarante :](https://ajuda.sankhya.com.br/hc/article_attachments/42865101884951)

   - Selecione a **Empresa** para a qual o processo será cadastrado.
   - Marque **Há responsabilidade indireta?** quando o declarante possuir responsabilidade indireta no processo.

     Nesse caso, informe o **Tipo de inscrição** (CPF/CNPJ)  e o **Número da inscrição** do responsável direto.
   - Caso o processo já tenha sido enviado pelo Portal do eSocial, marque **Inclusão realizada via Portal do eSocial?** e informe o **Nº de Recibo eSocial (S-2500)**.

     Após informar o número do recibo, as alterações ou exclusões do cadastro e seus respectivos envios ao eSocial serão realizadas pelo Pessoal+.

     Para registrar no sistema um processo que já foi enviado pelo Portal do eSocial, acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha), localize a referência do processo trabalhista e **realize apenas a geração do evento S-2500**. Não é necessário realizar o envio pelo sistema.

     Quando o evento S-2500 for gerado e enviado pelo Pessoal+, esses campos ficarão desabilitados para edição, pois todo o procedimento será realizado pelo sistema.
5. Preencha as **Informações do Processo:**

   [GIF animado: Imagem 3: Preencha as Informações do Processo :](https://ajuda.sankhya.com.br/hc/article_attachments/42865230683799)

   - Selecione a **Origem do processo**:

     - **Processo judicial:** informe a data da sentença e os dados da vara.
     - **Demanda submetida à CCP ou NINTER:** informe a data de conciliação, o âmbito de celebração do acordo e, quando aplicável, o CNPJ do sindicato.
   - Informe no campo **Número do Processo**, o número do processo trabalhista, da ata ou número de identificação da conciliação.
   - Se necessário, descreva **Observações** relacionadas ao processo.
6. Cadastre as **Informações do Trabalhador**:

   [GIF animado: Imagem 4: Cadastre as Informações do Trabalhador :](https://ajuda.sankhya.com.br/hc/article_attachments/42865998274071)

   - Informe os dados do trabalhador e, quando aplicável, seus dependentes.

     Para trabalhador contratado pelo declarante, marque **Trabalhador contratado pelo declarante** e pesquise o colaborador pelo código. Os dados serão preenchidos automaticamente.

     Quando o trabalhador **não for contratado pelo declarante**, os dados deverão ser informados manualmente.
   - Após confirmar os dados do trabalhador, é possível cadastrar os dependentes:

     - para trabalhadores contratados pelo declarante, os dependentes podem ser importados através do botão **Importar novo Dependente**;
     - nos demais casos, devem ser cadastrados manualmente pelo botão **Incluir novo Dependente**.

     **📚**Consulte o artigo [**Inclusão de Dependentes do Trabalhador no Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42862840302615) para obter detalhes sobre esse procedimento.

     [GIF animado: Imagem 5: 📚 Consulte o artigo Inclusão de Dependentes do Trabalhador no Processo Trabalhista para obter detalhes sobre esse…](https://ajuda.sankhya.com.br/hc/article_attachments/42865994577559)

   Quando a marcação **Há responsabilidade indireta?** estiver habilitada no menu **Declarante**, será exibida a seção **Informações do trabalhador no responsável direto**.

   Nessa seção, informe:

   - **Matrícula no empregador de origem**;
   - **Data de admissão do trabalhador no empregador de origem**.

   Essas informações devem corresponder aos dados informados pelo empregador de origem (responsável direto) nos eventos S-2190, S-2200 ou S-2300 do trabalhador.
7. Cadastre as **Informações do Contrato de Trabalho**:

   [GIF animado: Imagem 6: Cadastre as Informações do Contrato de Trabalho :](https://ajuda.sankhya.com.br/hc/article_attachments/42866432778391)

   O menu permite cadastrar **um ou mais contratos de trabalho para o processo**, inclusive mais de um contrato para o mesmo trabalhador, conforme as informações reconhecidas ou determinadas no processo.

   📚Consulte o artigo [**Informações do Contrato de Trabalho no Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671) para obter detalhes sobre os tipos de contrato e o preenchimento das informações específicas.
8. Confira os dados cadastrados.

   Caso existam informações que precisam de ajuste, será apresentado o ícone **Exibir erros de validação**. Clique nesse ícone para consultar as informações que precisam ser corrigidas.
9. Após preencher todas as informações aplicáveis ao contrato, clique em **Confirmar cadastro**.

   Com o cadastro confirmado e sem erros de validação, o processo fica disponível para geração e envio do evento **S-2500** ao eSocial.
10. Após a confirmação do processo, é exibido o menu **Informações de Tributos Decorrentes**.

    Essa etapa deve ser preenchida quando houver valores de **Contribuição Previdenciária ou Imposto de Renda a recolher** decorrentes do processo e ainda não declarados ao eSocial.

    [GIF animado: Imagem 7: Essa etapa deve ser preenchida quando houver valores de Contribuição Previdenciária ou Imposto de Renda a recolher…](https://ajuda.sankhya.com.br/hc/article_attachments/42888583868567)

    📚Consulte o artigo [**Informações de Tributos Decorrentes de Processo Trabalhista**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351) para obter detalhes sobre o preenchimento.
11. Após finalizar o cadastro das informações, acesse a Central do eSocial para gerar e enviar os eventos correspondentes.

### 4. Pontos de Atenção

- Confira todas as informações antes de confirmar o processo.
- Caso existam erros de validação, utilize a opção **Exibir erros de validação** para consultar as informações que precisam ser ajustadas.
- O tipo de contrato deve corresponder à situação determinada no processo trabalhista.
- Quando o processo for enviado inicialmente pelo Portal do eSocial, informe o número do recibo no cadastro para que as alterações e exclusões posteriores possam ser realizadas pelo Pessoal+.
- **Um mesmo processo trabalhista pode ter mais de um contrato de trabalho para o mesmo trabalhador.** Nesse caso, cadastre os contratos correspondentes no menu **Informações do Contrato de Trabalho**, conforme as informações reconhecidas ou determinadas no processo.
- Ao cadastrar um **novo processo trabalhista** para um trabalhador, o sistema verifica se já existe cadastro com o mesmo **CPF**, **número de processo** ou **acordo CCP/NINTER**:
  - quando o processo anterior já tiver sido **enviado ao eSocial**, o sistema não permitirá um novo cadastro com esses mesmos dados;
  - quando o processo anterior **ainda não tiver sido enviado ao eSocial**, o novo cadastro será permitido e a validação ocorrerá no momento de salvar as **Informações do Contrato de Trabalho**. Nessa situação, o sistema atribuirá uma **sequência** para cada cadastro do mesmo processo.
- Quando houver mais de um cadastro para o mesmo processo ainda não enviado ao eSocial, o sistema tratará os registros considerando as respectivas sequências. No envio do **S-2500**, cada registro receberá uma sequência numérica (**ideSeqTrab**) iniciada em **001**, com até três dígitos, conforme as regras do eSocial ([MOS - versão S-1.3/pág 332](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)). Se for necessário excluir um processo que possua **sequência** no S-2500, o evento de exclusão utilizará a mesma sequência do cadastro original.
- O evento **S-2501** deve ser utilizado somente quando houver informações de tributos decorrentes do processo.
- Alterações em informações já enviadas ao eSocial podem gerar eventos de retificação ou exclusão, conforme o dado alterado.

### 5. Dicas de Usabilidade

- Tenha a decisão judicial, ata ou acordo em mãos antes de iniciar o cadastro.
- Confira se o processo está sendo cadastrado para a empresa declarante correta.
- Antes de finalizar, revise principalmente os dados do trabalhador e do contrato de trabalho.
- Quando houver mais de um contrato relacionado ao processo, confira a sequência e as informações de cada contrato antes do envio ao eSocial.
- Se o processo já tiver sido enviado pelo Portal do eSocial, tenha em mãos o número do recibo do S-2500.

## Perguntas Frequentes (FAQ)

**1. O que acontece depois de confirmar o processo?**

O processo passa para o status **Confirmado** e, não havendo erros de validação, fica disponível para geração e envio do evento S-2500 ao eSocial.

**2. Preciso preencher as Informações de Tributos Decorrentes em todos os processos?**

Não. Essa seção deve ser preenchida somente quando houver valores de Contribuição Previdenciária ou Imposto de Renda a recolher relacionados ao processo e ainda não declarados ao eSocial.

**3. Posso cadastrar mais de um contrato para o mesmo processo?**

Sim. A tela permite incluir um ou mais contratos de trabalho relacionados ao processo.

Quando houver múltiplos contratos para o mesmo trabalhador, consulte o artigo **Cadastro de Processo Trabalhista com Múltiplos Contratos para o Mesmo Trabalhador**.

**4. O que faço se aparecer um erro de validação?**

Clique em **Exibir erros de validação** para consultar as informações que precisam ser corrigidas. Após realizar os ajustes, finalize o cadastro novamente.

**5. Posso cadastrar outro processo para um trabalhador que já possui um processo enviado ao eSocial?**

O sistema realiza validações para evitar duplicidade. Quando já existir um processo enviado ao eSocial com o mesmo CPF, número do processo ou acordo CCP/NINTER, um novo cadastro não será permitido.

**6. Posso cadastrar novamente um processo que ainda não foi enviado ao eSocial?**

Sim. Quando o processo ainda não foi enviado ao eSocial, o sistema permite realizar um novo cadastro. Nesse cenário, a validação ocorre durante o preenchimento e salvamento das informações do contrato de trabalho, e cada cadastro poderá receber uma sequência para identificação no eSocial.

## Artigos Relacionados

- [Inclusão de Dependentes do Trabalhador no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42862840302615)
- [Informações do Contrato de Trabalho no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671)
- [Informações de Tributos Decorrentes de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351)
- [Consulta e Exclusão de Processos Trabalhistas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42844767586071)
