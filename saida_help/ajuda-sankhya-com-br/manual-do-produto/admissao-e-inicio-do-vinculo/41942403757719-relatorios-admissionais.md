---
id: "41942403757719"
titulo: "Relatórios Admissionais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41942403757719-Relat%C3%B3rios-Admissionais"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Admissão e Início do Vínculo"
atualizado_em: "2026-09-25T18:22:19Z"
rotulos: ["Configuração", "Relatórios Formatados", "Relatórios", "Funcionários", "ID: br.com.sankhya.cadastro.funcionarios", "FPRELPADFUNC", "FPRELATFUNC", "Configuração Funcionários", "Pessoal+", "Relatórios Admissionais", "Ficha de Registro do Funcionário", "FPRELATVERSOF", "Documentos Admissionais"]
---

# Relatórios Admissionais

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Cadastros > Configuração Funcionários > Outras Opções > Relatórios Admissionais
**ID da Tela:**br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A funcionalidade **Relatórios Admissionais** reúne os principais documentos relacionados ao cadastro do colaborador, permitindo consultá-los e exportá-los diretamente pela tela **Configuração Funcionários**.

Os relatórios são definidos pela própria empresa, podendo utilizar tanto os modelos padrão disponibilizados pelo sistema Sankhya Om quanto modelos personalizados.

O layout do relatório define como o documento será gerado e apresentado pelo sistema. Por isso, sua correta configuração é indispensável para garantir que os documentos sejam emitidos conforme o modelo esperado pela empresa.

Entre os relatórios que podem ser disponibilizados estão:

- Ficha de Registro do Funcionário;
- Verso da Ficha de Registro;
- Ficha de Atualização do Colaborador;
- Contratos;
- Ficha Financeira;
- Aviso de Férias;
- Holerites;
- Demais documentos admissionais configurados pela empresa.

### 2. Pré-requisitos

Antes de configurar os relatórios admissionais, verifique se:

- possui acesso às telas **Relatórios Formatados** e **Preferências** (Configurações > Avançado). Essa liberação é realizada pelo administrador do sistema na tela **Acessos** (Configurações > Controle de Acesso);
- possui permissão para alterar parâmetros do sistema;
- os relatórios já foram cadastrados na tela **Relatórios Formatados**.

### 3. Jornada de Uso

#### 3.1 Relatórios admissionais padrão Sankhya

| **⚠️** **Atenção**  Para utilizar os **relatórios padrão Sankhya**, verifique se os parâmetros abaixo estão em branco:   - **FPRELPADFUNC** - **FPRELATVERSOF**   Quando esses parâmetros estiverem em branco, o sistema utilizará automaticamente os modelos padrão disponibilizados pela Sankhya. |
| --- |

#### 3.2 Relatórios admissionais personalizados

A configuração dos **Relatórios Admissionais** personalizados é composta das seguintes etapas:

(3)**Baixar os relatórios padrão para consulta (opcional)**

Para utilizar como exemplo os **modelos padrão** disponibilizados pela Sankhya:

1. Acesse o **Painel de Configurações** (Pessoal+ > Configurações);
2. Clique em **Download de Relatórios Padrão** e faça o download dos modelos:

   - Ficha de Registro do Funcionário;
   - Relatório de Verso da Ficha do Funcionário.

     [GIF animado: Imagem 1: Relatório de Verso da Ficha do Funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/41945290271767)

#### **(3)**Cadastrar os relatórios formatados

1. Acesse a tela **Relatórios Formatados** (Configurações > Avançado);
2. Clique em **Adicionar Relatório** e crie um novo relatório;
3. Preencha a **Descrição** com um nome que facilite sua busca;
4. Salve o cadastro;
5. Clique em **Adicionar Arquivo** e anexe os layouts que compõem o relatório;
6. Escolha os arquivos e confirme.

   ![Imagem 2: Escolha os arquivos e confirme.](https://ajuda.sankhya.com.br/hc/article_attachments/41946016094999)

   | **⚠️** **Atenção**  Para o relatório **Ficha de Atualização de CTPS e Previdência Social** do colaborador, os arquivos devem ser inseridos obrigatoriamente na seguinte ordem:  1. Ficha Atualização; 2. Salário; 3. Férias; 4. Contribuições Sindicais; 5. Afastamentos. A ordem dos arquivos deve ser respeitada. Caso contrário, a geração do documento poderá ser comprometida. |
   | --- |

#### 3.3 Configurar os parâmetros para relatórios personalizados

1. Após cadastrar os relatórios personalizados na tela **Relatórios Formatados**, acesse a tela **Preferências** (Configurações > Avançado).
2. Configure os parâmetros conforme a finalidade de cada um:

   - **Relatório Padrão de Funcionários - FPRELPADFUNC**:  informe no campo **Inteiro** apenas o código da **Ficha de Registro do Funcionário** que será utilizada como relatório padrão;
   - **Verso da ficha de reg. do Func. - FPRELATVERSOF**: informe no campo **Inteiro** apenas o código do relatório utilizado para o verso da **Ficha de Registro do Funcionário** padrão.
   - **Relatórios de Funcionários - FPRELATFUNC**: informe os códigos dos demais relatórios no campo **Texto** para serem exibidos na opção **Relatórios Admissionais** da tela **Configuração Funcionários**.

     ![Imagem 3: Relatórios de Funcionários - FPRELATFUNC : informe os códigos dos demais relatórios no campo Texto para serem exibidos…](https://ajuda.sankhya.com.br/hc/article_attachments/41946690272023)

     | **⚠️** **Atenção**  Para utilizar os **relatórios padrão Sankhya**, os parâmetros devem estar em branco. |
     | --- |

#### 3.4 Consultar e exportar os relatórios admissionais

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Selecione o colaborador;
3. Clique no botão **Outras Opções > Relatórios Admissionais**;
4. Na lista de documentos disponíveis para o colaborador, selecione um ou mais relatório(s) clicando em **Exportar Dados**;
5. Clique em **Exportar**.

   Caso deseje baixar todos os documentos apresentados, marque a opção **Selecionar todos** antes de **Exportar**.

   [GIF animado: Imagem 4: Caso deseje baixar todos os documentos apresentados, marque a opção Selecionar todos antes de Exportar .](https://ajuda.sankhya.com.br/hc/article_attachments/41947625684375)

   | ℹ️ **Nota**  Ao utilizar a opção **Selecionar todos**, se algum relatório não puder ser gerado, os demais serão exportados normalmente. Ao final do processo, o sistema apresentará uma mensagem informando quais documentos não puderam ser baixados. |
   | --- |

### 4. Pontos de Atenção

- Somente os relatórios personalizados informados no parâmetro **FPRELATFUNC** serão exibidos na opção Relatórios Admissionais.
- Para utilizar os modelos de relatório da ficha de registro padrão Sankhya, mantenha os parâmetros FPRELPADFUNC e FPRELATVERSOF em branco.
- Os layouts utilizados pelos relatórios devem estar corretamente cadastrados na tela **Relatórios Formatados** (Configurações > Avançado).
- A sequência dos arquivos da **Ficha de Atualização do Colaborador** deve ser respeitada para garantir a geração correta do documento.

### 5. Dicas de Usabilidade

- Utilize descrições padronizadas para facilitar a identificação dos relatórios.
- Revise os layouts sempre que houver alterações em documentos admissionais da empresa.
- Após incluir novos relatórios, valide sua geração antes de disponibilizá-los aos colaboradores.
- Mantenha apenas os documentos realmente utilizados pela empresa para facilitar a navegação.

## Perguntas Frequentes (FAQ)

**1. Onde os Relatórios Admissionais ficam disponíveis?**

Na tela **Configuração de Funcionários**, botão **Outras Opções > Relatórios Admissionais**.

**2. Posso utilizar relatórios personalizados?**

Sim. Basta cadastrá-los na tela **Relatórios Formatados** e informar seus códigos no parâmetro **FPRELATFUNC**.

**3. Para que serve o parâmetro FPRELATFUNC?**

Ele define quais relatórios serão apresentados ao usuário na opção **Relatórios Admissionais**.

**4. Para que serve o parâmetro FPRELPADFUNC?**

Ele define qual será a **Ficha de Registro do Funcionário** utilizada como relatório padrão.

**5. É possível baixar vários relatórios ao mesmo tempo?**

Sim. Selecione os documentos desejados e clique em **Exportar**.

**6. O que acontece se um relatório não puder ser gerado?**

Os demais relatórios serão exportados normalmente e o sistema informará quais documentos não puderam ser gerados.

**7. Preciso utilizar os modelos padrão da Sankhya?**

Não. Os modelos padrão são opcionais. A empresa também pode utilizar layouts personalizados cadastrados na tela **Relatórios Formatados** (Configurações > Avançado).

**8. Um relatório cadastrado em Relatórios Formatados não aparece na opção Relatórios Admissionais. O que verificar?**

Verifique se:

- o relatório foi cadastrado corretamente na tela **Relatórios Formatados**;
- o código do relatório foi informado no parâmetro **FPRELATFUNC**;
- no caso da ficha de registro do colaborador, se os parâmetros **FPRELPADFUNC** e **FPRELATVERSOF** estão configurados conforme o tipo de relatório utilizado (padrão ou personalizado);
- possui permissão de acesso às telas relacionadas.
