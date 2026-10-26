---
id: "31144991936151"
titulo: "Quitação de férias por afastamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151-Quita%C3%A7%C3%A3o-de-f%C3%A9rias-por-afastamento"
trilha: "Manual do Produto > Pessoas+ > Férias > Configuração e Regras de Férias"
atualizado_em: "2026-10-14T11:39:14Z"
rotulos: ["Ocorrências", "CLT", "Folha de Pagamento", "Férias", "afastamento", "pessoal+", "Rotina de Quitação de Férias em caso de Afastamento (Pessoal+)", "quitação de férias", "FPQUITAFERABERT"]
---

# Quitação de férias por afastamento

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.Ocorrencias

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A rotina de quitação de férias é utilizada quando o colaborador permanece afastado por período igual ou superior a **180 dias**, nas situações previstas pelo **Art. 133 da CLT**.

Quando configurada, o Pessoas+ realiza o processamento da quitação do período aquisitivo de férias relacionado ao afastamento e ajusta os períodos aquisitivos do colaborador após o retorno.

| **⚠️** **Atenção**  Esta regra é diferente do **Bloqueio de Cálculo de Férias para Funcionários Afastados**. O bloqueio impede o cálculo de férias durante um afastamento incompatível, enquanto a quitação trata do ajuste do período aquisitivo em afastamentos de longa duração. |
| --- |

### 2. Pré-requisitos

- O parâmetro **Quita férias na abertura para afastados - FPQUITAFERABERT** deve estar habilitado na tela **Preferências** (Configurações > Avançado).
- A ocorrência utilizada para o afastamento deve estar com a opção **Quita Férias por Afastamentos – Art. 133 CLT** marcada.
- O afastamento deve ser lançado na tela **Ocorrências** (Pessoal+ > Rotinas Folha).
- O campo **Data de Término** da ocorrência deve permanecer sem preenchimento enquanto o colaborador estiver afastado.

### 3. Jornada de Uso

#### Configurar a ocorrência

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Localize ou cadastre a ocorrência que será utilizada para o afastamento.
   - Na aba **Cadastro**, marque a opção **Quita Férias por Afastamentos - Art. 133 CLT.**

     ![Imagem 1: Na aba Cadastro , marque a opção Quita Férias por Afastamentos - Art. 133 CLT.](https://ajuda.sankhya.com.br/hc/article_attachments/35487698656919)

#### Lançar o afastamento

1. Volte a aba **Lançamento**.
2. Realize o lançamento da ocorrência para o colaborador.

   Enquanto o colaborador estiver afastado, **não preencha a** **Data de término**.

   ![Imagem 2: Enquanto o colaborador estiver afastado, não preencha a Data de término .](https://ajuda.sankhya.com.br/hc/article_attachments/31593841267479)

   | **⚠️** **Atenção**  A **Data de término** deve ser informada somente quando o colaborador retornar efetivamente do afastamento. Se esse campo for preenchido antes do retorno, o sistema não realizará o processo de quitação conforme esperado. |
   | --- |

#### Aguardar o processamento da quitação

Após o lançamento do afastamento, o sistema realiza automaticamente o processamento da quitação por meio de um **processo automático**, normalmente executado durante a noite.

Dessa forma, a quitação pode ser conferida no dia seguinte ao lançamento do afastamento.

Também é possível executar o processo manualmente pelo botão **Rodar Quitação de Férias, Atualiza Regras, Atualiza Liderança** da tela **Painel de Configurações**.

![Imagem 3: Também é possível executar o processo manualmente pelo botão Rodar Quitação de Férias, Atualiza Regras, Atualiza…](https://ajuda.sankhya.com.br/hc/article_attachments/31593794531223)

#### Conferir o período aquisitivo durante o afastamento

Enquanto o colaborador estiver afastado, não será possível calcular férias para o período que estiver sujeito à quitação.

Ao tentar realizar o cálculo, o sistema apresentará uma mensagem informando a situação.

![Imagem 4: Ao tentar realizar o cálculo, o sistema apresentará uma mensagem informando a situação.](https://ajuda.sankhya.com.br/hc/article_attachments/31144991915671)

Caso seja selecionada a opção **Sim** para prosseguir, o período aquisitivo correspondente não será apresentado para cálculo.

![Imagem 5: Caso seja selecionada a opção Sim para prosseguir, o período aquisitivo correspondente não será apresentado para…](https://ajuda.sankhya.com.br/hc/article_attachments/31593794541207)

E se mesmo assim tentar calcular as férias, será apresentada a seguinte mensagem:

![Imagem 6: E se mesmo assim tentar calcular as férias, será apresentada a seguinte mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/31144991916439)

Já na tela **Requisições > Férias,** na aba **Aquisitivos** ficará da seguinte forma:

![Imagem 7: Já na tela Requisições > Férias, na aba Aquisitivos ficará da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/31593794542871)

#### Encerrar o afastamento e concluir o ajuste

Quando o colaborador retornar do afastamento:

1. Edite a ocorrência de afastamento.
2. Informe a **Data de término** correspondente ao retorno do colaborador.

   Após o preenchimento da **Data de término**, o sistema conclui o ajuste do período aquisitivo e da quitação de férias relacionada ao afastamento.

   ![Imagem 8: Após o preenchimento da Data de término , o sistema conclui o ajuste do período aquisitivo e da quitação de férias…](https://ajuda.sankhya.com.br/hc/article_attachments/31593841274263)![Imagem 9: Após o preenchimento da Data de término , o sistema conclui o ajuste do período aquisitivo e da quitação de férias…](https://ajuda.sankhya.com.br/hc/article_attachments/31593794545175)

   | **⚠️** **Atenção**  Se a **Data de término** não for preenchida após o retorno do colaborador, o sistema não conclui o ajuste do período aquisitivo nem a quitação de férias relacionada ao afastamento.  Se um período aquisitivo não for ajustado corretamente após o retorno, verifique primeiro se a **Data de término** da ocorrência foi preenchida. |
   | --- |

   A tabela de férias do colaborador será atualizada automaticamente:

   - o período aquisitivo relacionado ao afastamento será apresentado como quitado, com a data final ajustada conforme o término do afastamento;
   - um novo período aquisitivo será iniciado no dia seguinte ao término do afastamento.

   A a tela **Requisições > Férias,** na aba **Aquisitivos** ficará da seguinte forma:

   ![Imagem 10: A a tela Requisições > Férias, na aba Aquisitivos ficará da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/31593794549015)

### 4. Pontos de Atenção

- A **Data de término** deve permanecer em branco durante o afastamento e ser preenchida somente após o retorno do colaborador.
- Se a **Data de término** for informada indevidamente durante o afastamento, o sistema não realizará o processo de quitação conforme esperado.
- Após o retorno, a **Data de término** deve ser informada para que o sistema conclua o ajuste do período aquisitivo.
- Se o período aquisitivo ou o processamento da folha continuarem bloqueados mesmo após o preenchimento da **Data de término**, verifique se o afastamento é do tipo **licença maternidade com prorrogação (tipo 18 - Empresa Cidadã)**, pois esse tipo de afastamento possui uma forma própria de encerramento.

### 5. Dicas de Usabilidade

- Se precisar validar a quitação antes da execução automática, utilize o botão **Rodar Quitação de Férias, Atualiza Regras, Atualiza Liderança**, disponível no **Painel de Configurações**.
- Após o retorno do colaborador, confira a **Data de término** da ocorrência antes de verificar o ajuste dos períodos aquisitivos.
- Consulte a tela **Requisições > Férias > Aquisitivos** para conferir os períodos aquisitivos do colaborador.

## Perguntas Frequentes (FAQ)

**1. Por que as férias do colaborador não foram quitadas durante o afastamento?**

Verifique se:

- o parâmetro **FPQUITAFERABERT** está habilitado;
- a ocorrência possui a opção **Quita Férias por Afastamentos - Art. 133 CLT** marcada;
- a ocorrência de afastamento foi lançada corretamente;
- a **Data de término** não foi preenchida enquanto o colaborador permanece afastado.

Se necessário, execute manualmente o processo pelo botão **Rodar Quitação de Férias, Atualiza Regras, Atualiza Liderança**, no **Painel de Configurações**.

**2. Preciso preencher a Data de término quando lançar o afastamento?**

Não. A **Data de término** deve permanecer em branco enquanto o colaborador estiver afastado. Ela deve ser preenchida somente quando ocorrer o retorno do colaborador.

**3. O que acontece quando informo a Data de término após o retorno?**

O sistema conclui o ajuste do período aquisitivo relacionado ao afastamento e cria o novo período aquisitivo a partir do dia seguinte ao término do afastamento.

**4. O período aquisitivo não foi ajustado após o retorno. O que verificar?**

Verifique se a **Data de término** da ocorrência de afastamento foi preenchida corretamente. Esse é um dos requisitos para que o sistema conclua o ajuste do período aquisitivo.

## Artigos Relacionados

- [Cadastro de Ocorrências para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Lançamento de Ocorrências para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/42603052607255-Lan%C3%A7amento-de-Ocorr%C3%AAncias-para-o-Colaborador)
- [Bloqueio do cálculo de férias para colaboradores afastados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42521124311575)
