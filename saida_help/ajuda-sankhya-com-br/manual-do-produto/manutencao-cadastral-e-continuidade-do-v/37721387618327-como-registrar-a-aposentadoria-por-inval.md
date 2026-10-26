---
id: "37721387618327"
titulo: "Como registrar a aposentadoria por invalidez"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37721387618327-Como-registrar-a-aposentadoria-por-invalidez"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Manutenção Cadastral e Continuidade do Vínculo"
atualizado_em: "2026-10-13T14:54:05Z"
rotulos: ["INSS", "eSocial", "Folha de Pagamento", "Benefício", "FGTS", "Aposentadoria"]
---

# Como registrar a aposentadoria por invalidez

### O que é e para que serve

A **aposentadoria por invalidez**, atualmente chamada de **aposentadoria por incapacidade permanente**, é um benefício do **INSS** concedido ao trabalhador que, após avaliação médica, é considerado permanentemente incapaz de exercer atividade que garanta sua subsistência, previsto no artigo 42 da Lei n.º 8.213/91.

Para a empresa, a concessão do benefício **não encerra o contrato de trabalho**. O contrato fica suspenso enquanto durar a aposentadoria.

No **Pessoas+**, a aposentadoria é registrada como uma **ocorrência de afastamento**. Não é necessário cadastrar um evento de folha específico para ela. Ao lançar a ocorrência, o sistema passa a considerar o colaborador como afastado, altera sua situação e prepara as informações para o envio ao eSocial.

Para ter direito à aposentadoria, o trabalhador precisa atender a alguns requisitos:

- **Ser segurado do INSS**: é necessário estar contribuindo para o INSS ou estar no período de graça, que é quando a pessoa já contribuiu, mas ainda mantém o vínculo com a Previdência Social.
- **Comprovar a incapacidade**: o trabalhador passa por uma perícia médica do INSS, que avalia se ele está realmente incapaz de trabalhar de forma permanente.
- **Cumprir a carência**: em regra, é preciso ter no mínimo 12 contribuições mensais ao INSS.

  Conforme a Portaria MTP/MS n.º 22/2022, esse prazo não é exigido quando a incapacidade ocorre por:

  - Acidente de trabalho;
  - Doença causada pelo trabalho;
  - Doenças graves previstas em lei.

| ℹ️ **Nota**  **Diferença entre aposentadoria por invalidez e auxílio-doença**  A diferença entre os dois benefícios está no **tempo da incapacidade**, avaliado pela perícia médica do INSS.   - **Aposentadoria por invalidez**: quando o trabalhador está **permanentemente incapaz** para o trabalho. - **Auxílio-doença**: quando a incapacidade é **temporária**. |
| --- |

###

Depois que o INSS conceder a aposentadoria, o colaborador deve apresentar à empresa a documentação que comprove o benefício e, principalmente, a **data de início da aposentadoria**.

A empresa deve:

1. Registrar a aposentadoria como afastamento no Pessoas+.
2. Informar a data de início conforme a concessão do INSS.
3. Manter o afastamento aberto enquanto o benefício estiver vigente.
4. Enviar as informações ao eSocial.
5. Ajustar os processos de folha, férias e provisões conforme o afastamento.

| ℹ️ **Nota**  O pedido do benefício é feito pelo trabalhador ao INSS. A empresa não solicita a aposentadoria em nome do colaborador. O pedido é realizado pelo **Meu INSS**, e a análise do benefício é feita pelo INSS. |
| --- |

### Antes de começar

Confira se você tem:

- **Carta de concessão do INSS**, com a data de início da aposentadoria.
- Acesso às telas **Código de Afastamento** (Pessoal+ > Cadastros) e **Ocorrências** (Pessoal+ > Rotinas Folha);

  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- O parâmetro **Quita férias na abertura para afastados - FPQUITAFERABERT** habilitado na tela **Preferências** (Configurações > Avançado), caso a empresa utilize a quitação automática de férias.

### Como registrar a aposentadoria por invalidez no Pessoas+

#### 1. Configure o código de afastamento

1. Acesse a tela **Código de Afastamento** (Pessoal+ > Cadastros).
2. Localize o código utilizado para a aposentadoria por invalidez ou cadastre-o, conforme a configuração adotada pela empresa.

   📚Para mais detalhes desse cadastro, acesse [**Cadastro de Códigos de Afastamento para Rescisão**](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487).
3. Confira principalmente:

   - **Código Governamental:** deve corresponder ao código oficial do motivo de afastamento;
   - **Direito ao décimo terceiro:** deixe desmarcado;
   - **Direito a multa do FGTS:** deixe desmarcado.

#### 2. Configure a ocorrência

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Localize ou cadastre a ocorrência **Aposentadoria por invalidez**.

   ![Imagem 1: Localize ou cadastre a ocorrência Aposentadoria por invalidez .](https://ajuda.sankhya.com.br/hc/article_attachments/37725297125399)

   Na configuração:

   1. Informe, no campo **Descrição E-Social**, o motivo **06 – Aposentadoria por invalidez**, conforme a Tabela 18 do eSocial.
   2. Nas **Propriedades da Ocorrência**, marque **Quita Férias por Afastamentos – Art. 133 CLT** e **Baixa na Provisão**, uma vez que esse afastamento irá quitar as férias.
   3. Confirme as alterações.

#### 3. Lance a ocorrência de aposentadoria para o colaborador

1. Depois de configurar a ocorrência, acesse a aba **Lançamento** dessa mesma tela e faça o lançamento para o colaborador.

   ![Imagem 2: Depois de configurar a ocorrência, acesse a aba Lançamento dessa mesma tela e faça o lançamento para o colaborador.](https://ajuda.sankhya.com.br/hc/article_attachments/37725850511383)
   1. Selecione a empresa.
   2. Localize o colaborador.
   3. Lance a ocorrência **Aposentadoria por invalidez**.
   4. Informe como **Data de início** a data indicada pelo INSS.
   5. **Não informe a Data de término.**
   6. Confirme o lançamento.

      O afastamento deve permanecer aberto enquanto a aposentadoria estiver vigente.

      | 💡 **Dica**  Se o colaborador estava afastado por auxílio-doença, encerre esse afastamento antes. Informe a **Data de término** no dia anterior ao início da aposentadoria. |
      | --- |

#### 4. Envie o afastamento ao eSocial

1. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha).
2. Gere e nvie:

   - a **alteração da situação** do colaborador, para que ele deixe de constar como ativo no portal do eSocial;
   - o evento **S-2230 – Afastamento Temporário**, com a ocorrência de aposentadoria por invalidez.

Fique atento:

- O S-2230 é o único evento que informa o afastamento. Não existe um envio separado de alteração de situação.
- Como a aposentadoria não tem data de fim, o evento é enviado apenas com a data de início.
- Se a ocorrência não tiver o motivo eSocial preenchido, o S-2230 não é gerado.
- O envio do motivo **06 – Aposentadoria por invalidez** é **obrigatório** para empregados (categorias 1XX) e **facultativo** para as categorias 3XX.

### Como o Pessoas+ trata o colaborador aposentado

Enquanto o colaborador estiver com o registro de ocorrência **Aposentadoria por Invalidez** em aberto (sem data fim), seu cadastro terá os seguintes dados:

- **Situação:** Aposentadoria por Invalidez
- **Aba Afastamento**

  - **Causa do Afastamento:** 70 Aposentadoria
  - **Motivo do Afastamento para FGTS:** 50 Aposent. com cont. de vinc. empregatício
  - **Motivo do Afastamento para RAIS:** 232 Apos. invalidez exceto p/ ac. trabalho![Imagem 3: Motivo do Afastamento para RAIS: 232 Apos. invalidez exceto p/ ac. trabalho](https://ajuda.sankhya.com.br/hc/article_attachments/37727125376151)

O colaborador aposentado continua no cálculo da folha, mas só recebe valores no mês de início. Os dias afastados são descontados desde o primeiro dia. **Não existem os 15 dias pagos pela empresa**, como no afastamento por doença ou acidente.

| Item | **Como o Pessoas+ trata** |
| --- | --- |
| **Salário no mês de início** | Calcula só os dias anteriores à aposentadoria. |
| **Salário, INSS e FGTS nos meses seguintes** | Não calcula, porque não há remuneração. |
| **13º salário** | Perde o avo no mês com menos de 15 dias trabalhados, desde que **Direito ao décimo terceiro** esteja desmarcado na tela Código de Afastamento. O 13º salário do período afastado é pago pelo INSS. |
| **Férias** | Enquanto a aposentadoria estiver ativa, o cálculo de férias fica bloqueado.  Com a configuração de **Quita Férias por Afastamentos – Art. 133 CLT**, o sistema realiza a quitação do período aquisitivo conforme o tratamento previsto para o afastamento.   | 💡 **Dica**  O período aquisitivo é quitado quando o afastamento passa de **180 dias**. O processamento roda automaticamente durante a noite, e o resultado pode ser conferido no dia seguinte.  Se precisar atualizar o resultado imediatamente, utilize o botão **Rodar Quitação de Férias, Atualiza Regras, Atualiza Liderança**, disponível no **Painel de Configurações**. | | --- | |
| **Provisão de férias e 13º** | Não provisiona novos avos a partir do afastamento.  Mas, inclua o colaborador aposentado no **cálculo da provisão em lote todo mês**, mesmo sem valores novos. Se uma referência ficar sem provisão calculada, o saldo atual do relatório de provisão fica divergente.  Depois, faça a integração normalmente em **Gerenciador de Folhas > Provisão de Férias e 13º > Integração Contábil Provisões**. |
| **Plano de saúde** | Se o colaborador possuía plano de saúde empresarial, o benefício deve ser mantido durante a aposentadoria.  Como não haverá folha para realizar o desconto da participação do colaborador, essa cobrança deve ser tratada fora da folha. |
| **Vale-refeição e vale-alimentação** | O cálculo não considera a situação do colaborador. Para zerar o benefício no afastamento, a regra precisa desconsiderar afastamentos e ter o tipo de afastamento cadastrado. Se a regra usar desconto em valor fixo, o desconto pode continuar sendo gerado mesmo com o benefício zerado. |

### Retorno do colaborador

Quando o INSS cancela a aposentadoria, o colaborador volta ao trabalho. O retorno é registrado encerrando a ocorrência.

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Clique no card do colaborador para ver o histórico.
3. Selecione a ocorrência de aposentadoria por invalidez.
4. Clique em **Editar Ocorrência**.
5. Informe a **Data de término** (o dia anterior ao retorno).
6. Confirme o lançamento.
7. Em **Configuração Funcionários > Afastamento**, confira se a situação voltou para **Atividade normal**.
8. Na **Central do eSocial**, faça a geração e envie o **S-2230** de término do afastamento.

Ao informar a Data de término, o Pessoas+ automaticamente:

- volta a situação do colaborador para **Atividade normal**;
- limpa os dados de afastamento do cadastro do colaborador;
- remove as quitações de férias posteriores ao retorno;
- inicia um novo período aquisitivo no dia seguinte ao término. Confira em **Requisições > Férias**, aba **Aquisitivos**.

| 💡 **Dica**  Antes de calcular a próxima folha, revise salário, cargo e benefícios do colaborador. |
| --- |

### Depois do retorno: cálculo da rescisão

Enquanto a aposentadoria estiver ativa, o contrato permanece suspenso e **não deve ser calculada a rescisão**.

O próprio Pessoas+ bloqueia o cálculo enquanto existir um afastamento sem **Data de término**.

Depois de registrar o retorno:

1. Calcule a rescisão utilizando o tipo correspondente ao **motivo real do desligamento**, por exemplo, dispensa sem justa causa ou pedido de demissão.
2. Informe uma data de desligamento posterior à **Data de término** do afastamento.
3. Envie o evento **S-2299** ao eSocial.

   | **⚠️** **Atenção**  Para empregado CLT que retornou da aposentadoria, não utilize automaticamente o motivo de desligamento 39. Esse motivo é destinado ao servidor estatutário. Para empregados, informe o motivo real do desligamento. |
   | --- |

### Pontos de atenção

- **Não informe a Data de término** enquanto o colaborador estiver aposentado.
- **Preencha o motivo eSocial.** Sem a **Descrição E-Social** na ocorrência, o S-2230 é rejeitado com o Erro 239 – Motivo do afastamento inválido.
- Não tente calcular férias enquanto o afastamento estiver aberto.
- Inclua o colaborador no cálculo mensal das provisões.
- Antes de calcular uma rescisão após o retorno, verifique se existe algum período de estabilidade aplicável ao caso.
- **Confira a data de desligamento.** Ela não pode ser igual à Data de término do afastamento nem estar dentro do período afastado. Nesses casos, o S-2299 é rejeitado com o Erro 191 – Não é permitido o desligamento do trabalhador.

### Perguntas Frequentes

**1. Preciso cadastrar um evento de folha para a aposentadoria por invalidez?**

Não. A aposentadoria é registrada como uma **ocorrência de afastamento**, vinculada a um código de afastamento.

**2. Depois de lançar a ocorrência, a informação já vai para o eSocial?**

Não. É necessário enviar a alteração da situação e o **S-2230** pela Central do eSocial.

**3. O colaborador aparece na folha no período da aposentadoria?**

Somente no mês em que a aposentadoria começa, para os dias trabalhados antes do início do afastamento. Nos meses seguintes, enquanto permanecer afastado, não são calculados salário, INSS e FGTS pela folha da empresa.

**4. Posso calcular férias para o colaborador aposentado?**

Não. O cálculo fica bloqueado enquanto a ocorrência de aposentadoria estiver aberta.

**5. Posso calcular a rescisão enquanto o colaborador está aposentado?**

Não. Primeiro é necessário registrar o retorno, encerrando a ocorrência de afastamento. Depois disso, a rescisão pode ser calculada.

**6. O que acontece com as férias quando o colaborador retorna?**

Ao informar a Data de término, o Pessoas+ conclui a quitação do período correspondente ao afastamento e inicia um novo período aquisitivo no dia seguinte ao término.

**7. Por quanto tempo a ocorrência deve permanecer aberta?**

A ocorrência deve permanecer aberta enquanto durar a aposentadoria. Quando o INSS determinar o retorno do colaborador, registre a Data de término e faça o envio do retorno ao eSocial.

### Artigos Relacionados

- [Cadastro de Códigos de Afastamento para Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487)
- [Bloqueio do cálculo de férias para colaboradores afastados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42521124311575)
- [Quitação de férias por afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151)
- [Como editar as ocorrências lançadas para um colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407377343127)
- [Erro ao calcular rescisão de funcionário afastado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39396275007639)
- [Como fazer a integração contábil da provisão de férias e 13º](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727)
