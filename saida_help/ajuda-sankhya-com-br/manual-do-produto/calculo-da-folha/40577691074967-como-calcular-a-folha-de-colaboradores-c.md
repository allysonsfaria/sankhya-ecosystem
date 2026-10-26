---
id: "40577691074967"
titulo: "Como calcular a folha de colaboradores com múltiplos contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-10-02T15:36:23Z"
rotulos: ["Configuração", "Contrato", "Impostos", "Folha", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Pessoal+", "Cálculo para Múltiplos Contratos"]
---

# Como calcular a folha de colaboradores com múltiplos contratos

**Módulo:** Pessoal+
**Versão Mínima:**5.103
**Caminho de Acesso:**Pessoal+ › Rotinas Folha › Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KRZZBMF4PJCWVGEK08WEJRY6)

[Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KRZZ2S7JPVS7NEVDH16SG80B)
[Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KRZZ2S7TBE8N30EKG5JEPX6Y)
[Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KRZZ2S8PVDNE5D49AEFXH09C)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KS0D7S5MQ0QF774X9NZCWHYE)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/40577691074967-Como-calcular-a-folha-de-colaboradores-com-m%C3%BAltiplos-contratos#h_01KS012G92D45R3ZVVNQY362Q8)

---

## Descrição e Usabilidade

A rotina de **Cálculo para Múltiplos Contratos** identifica trabalhadores com mais de um vínculo ativo para o mesmo empregador e CPF, automatizando a apuração de INSS e IRRF. Ela serve para garantir que o desconto de INSS não ultrapasse o teto legal e que o IRRF seja calculado sobre a base consolidada dos rendimentos. Este processo **não** se aplica a vínculos de empregadores diferentes (CNPJ raiz distintos).

O sistema considera que um trabalhador possui **múltiplos contratos** quando:

- possui o **mesmo CPF**;
- os contratos pertencem ao **mesmo empregador**, identificado pela mesma empresa matriz (mesmo CNPJ raiz);
- existam dois ou mais contratos ativos simultaneamente.

Também será considerado múltiplo contrato quando houver, na mesma competência da folha, um contrato ativo e outro desligado, desde que o desligamento tenha ocorrido na mesma competência da nova admissão.

**Exemplo**

| Situação | É considerado múltiplo contrato? |
| --- | --- |
| Dois contratos ativos na mesma empresa matriz | Sim |
| Contrato ativo e outro desligado na mesma competência | Sim |
| Transferência para outra filial do mesmo empregador, sem coexistência de contratos ativos | Não |

| **⚠️** **Atenção**  Uma transferência entre empresas do mesmo empregador não caracteriza múltiplo contrato quando existe continuidade contratual e apenas um vínculo permanece ativo. |
| --- |

### Pré-requisitos

Antes de processar a folha, garanta que:

- A opção **Considerar múltiplos contratos nos cálculos** esteja marcada como **Sim** no cadastro da empresa matriz (Pessoal+ > Cadastros > Empresas).
- As filiais estejam corretamente vinculadas à empresa matriz.
- Os contratos do trabalhador estejam cadastrados com o mesmo CPF e para o mesmo empregador (mesmo CNPJ raiz).
- Para trabalhadores autônomos, os Recibos de Pagamento de Autônomo (RPAs) da competência já tenham sido calculados, ou o sistema bloqueia o cálculo.

### Jornada de Uso

A rotina é automática após a ativação. Siga os passos para configurar e validar o processo.

#### 1. Ative a rotina na empresa matriz

1. Acesse a tela **Empresas** (Pessoal+ > Cadastros);
2. Selecione a empresa matriz;
3. Na aba **Informações Gerais**, ative a opção **Considerar múltiplos contratos nos cálculos**.

   ![Imagem 1: Na aba Informações Gerais , ative a opção Considerar múltiplos contratos nos cálculos .](https://ajuda.sankhya.com.br/hc/article_attachments/41598008924695)

   | ℹ️ **Nota**  Esta configuração é centralizada. Uma vez ativada na matriz, ela é aplicada automaticamente a todas as filiais vinculadas, não sendo necessário repetir o processo. |
   | --- |

#### 2. Confira o cadastro dos trabalhadores

1. Na tela **Configuração Funcionários** (Pessoal+ > Cadastros), verifique se os dados abaixo estão corretos nos contratos que serão unificados no cálculo:
   - CPF;
   - Empresa e Filial;
   - Categoria do trabalhador (eSocial);
   - Data de admissão;
   - Data de desligamento, quando houver;
   - Situação do contrato.

     [GIF animado: Imagem 2: Situação do contrato.](https://ajuda.sankhya.com.br/hc/article_attachments/41599538703127)

#### 3. Processe o cálculo da folha

1. Acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha);
2. Execute o cálculo da folha normalmente.

   O sistema identificará os múltiplos contratos e aplicará a ordem de processamento automaticamente para recompor as bases de INSS e IRRF.

   A regra geral é:

   1. Contratos CLT são processados antes dos Contribuintes Individuais.
   2. O sistema verifica contratos do mesmo CPF e mesmo empregador.
   3. As bases de INSS e IRRF são recompostas.
   4. O INSS respeita o teto da categoria.
   5. O IRRF é calculado sobre a base consolidada real.

   | **⚠️** **Atenção**  Se um trabalhador autônomo tiver RPAs pendentes de cálculo na competência, o sistema irá bloquear o cálculo da folha mensal para ele com a mensagem:   "**Atenção! Cálculo não permitido. Calcule os RPA(s) antes de processar o mensal.**" |
   | --- |

#### 4. Conferência da(s) folha(s)

Após concluir o cálculo:

1. Acesse o **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha) e verifique se os cálculos foram processados corretamente.
2. Revise as mensagens informativas e advertências.
3. Em caso de exclusão ou recálculo, confirme se os cálculos dependentes foram tratados corretamente.
4. Confira demonstrativos, bases de INSS, bases de IRRF e eventos relacionados antes de finalizar a folha.

   [GIF animado: Imagem 3: Confira demonstrativos, bases de INSS, bases de IRRF e eventos relacionados antes de finalizar a folha.](https://ajuda.sankhya.com.br/hc/article_attachments/41604834912919)

#### 5. Consulte a recomposição de bases

Para entender como o sistema consolidou os valores:

1. Acesse o card do colaborador e vá até a aba **Folha**;
2. Na grade, clique no ícone de detalhamento das **Bases** que você deseja analisar;
3. Na linha da **Base**, clique em **Eventos que compõem**;

   O sistema exibirá a origem dos valores, os contratos envolvidos na recomposição, os eventos que compuseram a base final e a diferença entre recomposição por múltiplos contratos e recomposição por data de pagamento entre folhas.

   [GIF animado: Imagem 4: O sistema exibirá a origem dos valores, os contratos envolvidos na recomposição, os eventos que compuseram a base final…](https://ajuda.sankhya.com.br/hc/article_attachments/41604868281239)

#### Exemplos práticos

**Exemplo 1: trabalhador com três contratos CLT**

Um trabalhador possui três contratos CLT no mesmo empregador.

- O sistema soma os rendimentos para recompor a base de INSS e IRRF.
- Se o primeiro contrato já atingir o teto de INSS, os contratos seguintes terão INSS igual a zero, evitando desconto acima do limite legal.
- O IRRF será calculado considerando a soma real dos rendimentos tributáveis e os descontos já realizados nos contratos anteriores.

**Exemplo 2: autônomo com RPA pendente**

A empresa está configurada para considerar múltiplos contratos. O usuário tenta calcular o mensal de autônomo sem calcular antes o RPA.

- O sistema bloqueia a ação e exibe a mensagem:

  **Atenção!**
  **Cálculo não permitido. Calcule os RPA(s) antes de processar o mensal.**

**Exemplo 3: exclusão de cálculo com dependência**

O usuário tenta excluir uma folha que impacta cálculos posteriores por recomposição de bases.

- O sistema identifica a dependência e apresenta uma mensagem para que o usuário decida se deseja excluir também os cálculos dependentes, evitando inconsistências em INSS, IRRF, demonstrativos e eventos relacionados.

### Pontos de Atenção

🔹**Validações realizadas no cadastro do trabalhador**

Ao cadastrar ou alterar um trabalhador que possua múltiplos contratos para o mesmo empregador, o sistema realiza validações adicionais para auxiliar na conferência das informações.

- **Limite da carga horária semanal**

  Para trabalhadores das categorias **101 (Empregado Geral)** e **111 (Empregado Intermitente)**, o sistema soma a carga horária semanal de todos os contratos ativos do mesmo empregador.

  Caso o total ultrapasse **44 horas semanais**, será apresentada uma mensagem de alerta para que você confirme se deseja continuar o cadastro.
- **Código da carga horária**

  Também é verificado se contratos CLT (categorias **101** e **111**) do mesmo empregador utilizam o mesmo código de carga horária.

  Quando houver duplicidade, o sistema apresentará um alerta, permitindo que você revise a informação antes de prosseguir.
- **Código da função**

  Quando a empresa utiliza código de função diferente de zero, o sistema verifica se múltiplos contratos CLT do mesmo empregador utilizam a mesma função.

  Caso isso ocorra, será apresentada uma mensagem de confirmação para que você decida se deseja prosseguir.

  | ℹ️ **Nota**  As validações de carga horária, código de carga horária e código de função são apenas informativas. Você pode optar por prosseguir com o cadastro após confirmar a mensagem apresentada pelo sistema. |
  | --- |
- **Categorias que possuem bloqueio para múltiplos contratos**

  Algumas categorias para o eSocial não permitem mais de um contrato ativo para o mesmo empregador:

  - 103 - Empregado Aprendiz;
  - 901 - Estagiário.

  As demais categorias continuam seguindo as regras de múltiplos contratos normalmente.

🔹**Validações no Importador Folha**

As mesmas regras também são consideradas durante a importação de colaboradores pelo **Importador Folha**.

Nesse processo:

- **Aprendiz (categoria 103)**: caso a importação identifique mais de um contrato ativo para o mesmo CPF e empregador, o registro será rejeitado e a ocorrência será registrada na planilha de erros.
- **Estagiário (categoria 901)**: caso exista mais de um contrato ativo para o mesmo CPF e empregador, o registro também será rejeitado e informado na planilha de erros.
- As validações referentes à carga horária semanal, código de carga horária e código de função **não bloqueiam a importação**. Os registros são importados normalmente, cabendo ao usuário revisar posteriormente as inconsistências apontadas, quando aplicável.

🔹**Validações nas Requisições Individuais**

Além das validações realizadas durante o cadastro e a alteração do trabalhador, o sistema também verifica situações de múltiplos contratos na **aprovação individual de requisições**, garantindo maior conformidade com a legislação trabalhista e consistência das informações.

Essas validações são aplicadas nas aprovações realizadas pelas seguintes rotinas:

- **Painel de Lideranças** (Pessoal+ > Rotinas Folha);
- **Gerenciador de DP** (Pessoal+ > Rotinas Folha).

  | **⚠️** **Atenção**  As validações descritas nesta seção são aplicadas apenas às aprovações individuais. As aprovações em lote ainda não contemplam esse comportamento. |
  | --- |

As seguintes requisições possuem validações específicas:

- **Requisição de Admissão**

O sistema identifica automaticamente se o CPF informado já possui outro contrato ativo para o mesmo empregador (mesma empresa matriz).

A aprovação será bloqueada quando existir outro contrato ativo nas seguintes categorias:

- **103 – Aprendiz**;
- **901 – Estagiário**.

Nesses casos, será apresentada uma mensagem informando que a legislação não permite a coexistência desses vínculos para o mesmo empregador.

- **Requisição de Alteração de Cargo e Salário**

  Quando o parâmetro **Onde Utiliza o CBO? (FPUTILIZACBO)** estiver configurado como **Função**, o sistema também valida a função informada na requisição.

  Caso exista outro contrato ativo para o mesmo CPF, na mesma empresa matriz, utilizando a mesma função, será apresentada uma mensagem de alerta permitindo que você:

  - prossiga com a aprovação; ou
  - cancele a operação para revisar a informação.

    | **⚠️** **Atenção**  Essa validação possui caráter informativo e não impede a aprovação da requisição. |
    | --- |
- **Requisição de Alteração Temporária de Carga Horária**

O sistema compara os contratos ativos do mesmo CPF pertencentes à mesma empresa matriz.

Essa validação é aplicada apenas aos trabalhadores das categorias:

- 101 – Empregado CLT;
- 111 – Empregado Intermitente.

A verificação considera o **código de carga horária vigente ou futuro**, registrado no histórico de carga horária do trabalhador.

Caso outro contrato ativo utilize o mesmo código de carga horária, será apresentada uma mensagem de alerta permitindo que você escolha entre prosseguir ou cancelar a aprovação.

Assim como na alteração de função, essa validação é apenas informativa.

🔹**Recálculo e exclusão de folhas com dependência**

A alteração em um contrato pode impactar os valores de outros. Por isso, o sistema possui travas de segurança.

- **Exclusão:** ao tentar excluir uma folha que serve de base para o cálculo de outro contrato, o sistema exibirá um alerta e perguntará se você deseja excluir também os cálculos dependentes.

  Para exclusão coletiva, o sistema também identifica cálculos com dependência, apresenta um popup de decisão e pode gerar uma planilha Excel com o resultado da operação.
- **Recálculo:** o recálculo coletivo **não** processa automaticamente folhas com dependência de múltiplos contratos.

  O sistema registrará uma advertência no Gerenciador de Folhas para que você faça o ajuste de forma manual e controlada.

🔹**Base legal para INSS e IRRF**

A recomposição de bases de INSS e IRRF segue as diretrizes da legislação previdenciária e da Receita Federal.

| ℹ️ **Nota**  Este processo visa garantir a conformidade com as obrigações legais, como o teto de contribuição do INSS e a tabela progressiva do Imposto de Renda. É fundamental que as categorias dos trabalhadores (eSocial) e os eventos (rubricas) estejam configurados corretamente. Para mais detalhes, consulte sempre a legislação vigente. |
| --- |

🔹**Alertas**

1. **O cálculo mensal do autônomo foi bloqueado**

   **Causa provável:** há RPA(s) não calculados.

   **Como resolver:** calcule todos os RPA(s) do trabalhador antes de processar o mensal. Depois, execute o cálculo novamente.
2. **O recálculo coletivo não processou algumas folhas**

   **Causa provável:** as folhas possuem múltiplos contratos com cálculos dependentes.

   **Como resolver:** consulte as advertências no Gerenciador de Folhas, revise os cálculos dependentes e realize o ajuste necessário de forma controlada.
3. **O sistema exibiu uma faixa informativa de recomposição**

   **Causa provável:** o trabalhador possui múltiplos contratos com bases dependentes de INSS ou IRRF.

   **Como resolver:** revise o cálculo relacionado e consulte o detalhamento das bases para entender quais contratos e eventos participaram da recomposição.
4. **A exclusão coletiva apresentou um popup de decisão**

   **Causa provável:** entre as folhas selecionadas existem cálculos com dependência.

   **Como resolver:** escolha uma das opções apresentadas pelo sistema: excluir todos os cálculos, incluindo dependentes, ou excluir apenas os cálculos sem dependência. Ao final, consulte a planilha gerada com o resultado.

## Perguntas Frequentes

**1. Preciso definir a ordem de cálculo dos contratos manualmente?**

Não. Com a rotina ativa, o sistema controla a ordem de processamento automaticamente para garantir a correta recomposição das bases.

**2. A configuração deve ser feita em todas as filiais?**

Não. A configuração realizada no cadastro da empresa matriz é aplicada automaticamente a todas as suas filiais.

**3. O sistema considera contratos de CNPJs diferentes?**

Sim, desde que os CNPJs pertençam ao mesmo empregador, ou seja, possuam o mesmo CNPJ raiz (os 8 primeiros dígitos).

**4. O salário-família entra na base de cálculo de INSS ou IRRF?**

Não. O benefício do salário-família não tem incidência de INSS nem de IRRF e seu cálculo é feito de forma separada para cada contrato.

**5. Por que o recálculo coletivo não processou a folha de um colaborador?**

Provavelmente porque essa folha possui dependência de múltiplos contratos. Verifique as advertências no Gerenciador de Folhas e realize o ajuste manualmente para garantir a consistência dos valores.

**6. O sistema impede cadastrar dois contratos para o mesmo CPF?**

Depende da categoria do trabalhador.

Para empregados CLT e demais categorias permitidas, o sistema realiza validações e apresenta alertas quando identifica situações que merecem conferência.

Já para as categorias **103 (Aprendiz)** e **901 (Estagiário)**, o sistema impede o cadastro de um segundo contrato ativo para o mesmo empregador.

**7. O que acontece se a soma das jornadas ultrapassar 44 horas semanais?**

O sistema apresenta uma mensagem de alerta informando que a soma das jornadas excede o limite legal.

A gravação do cadastro continua sendo permitida mediante confirmação do usuário.

**8. Posso utilizar o mesmo código de carga horária em dois contratos?**

Não é recomendado.

Quando contratos CLT (categorias 101 e 111) do mesmo empregador utilizam o mesmo código de carga horária, o sistema apresenta um alerta para que a informação seja revisada.

**9. Posso utilizar a mesma função em dois contratos?**

Quando a empresa utiliza código de função diferente de zero, o sistema verifica se existe outro contrato CLT para o mesmo empregador utilizando a mesma função.

Nessa situação é apresentada uma mensagem de confirmação antes da gravação do cadastro.

**10. Transferências entre filiais geram múltiplos contratos?**

Não necessariamente.

Quando ocorre apenas uma transferência entre empresas do mesmo empregador, sem coexistência de dois contratos ativos, o sistema não caracteriza essa situação como múltiplo contrato.

**11. As validações de múltiplos contratos também ocorrem nas requisições?**

Sim. Além do cadastro do trabalhador, o sistema realiza validações durante a aprovação individual de requisições de admissão, alteração de cargo e salário (por função) e alteração temporária de carga horária.

**12. As requisições em lote também possuem essas validações?**

Não. Nesta versão, as validações são executadas apenas nas aprovações individuais realizadas pelo Painel de Lideranças e pelo Gerenciador de DP.

**13. Quais situações impedem a aprovação de uma requisição?**

A aprovação é bloqueada quando a requisição resultar em mais de um contrato ativo para o mesmo empregador nas categorias **Aprendiz (103)** ou **Estagiário (901)**, conforme as regras legais aplicáveis.

**14. Quando o sistema apenas apresenta um alerta?**

São exibidos alertas, sem bloqueio da aprovação, quando são identificadas possíveis inconsistências relacionadas à:

- utilização da mesma função em múltiplos contratos CLT (quando o CBO é utilizado por função);
- utilização do mesmo código de carga horária em múltiplos contratos CLT.

## Artigos Relacionados

- [Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
