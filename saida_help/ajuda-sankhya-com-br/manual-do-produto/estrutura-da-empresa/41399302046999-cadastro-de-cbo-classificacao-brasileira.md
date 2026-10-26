---
id: "41399302046999"
titulo: "Cadastro de CBO (Classificação Brasileira de Ocupações)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Estrutura da Empresa"
atualizado_em: "2026-10-21T19:08:29Z"
rotulos: ["Configuração", "CBO", "Cargos", "br.com.sankhya.rh.CBO", "eSocial", "Cadastro", "Pessoal+", "Ocupações"]
---

# Cadastro de CBO (Classificação Brasileira de Ocupações)

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > CBO
**ID da tela:** br.com.sankhya.rh.CBO

---

## Sumário

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#antes-de-comecar)
- [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#jornada)
  1. [Cadastrar a CBO](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#etapa1)
  2. [Configurar o tipo do horário noturno](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#etapa2)
  3. [Vincular a CBO ao cargo ou à função](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#etapa3)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#pontos-de-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#faq)
- [Artigos relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es#relacionados)

---

### O que é e para que serve

A **Classificação Brasileira de Ocupações (CBO)** é a tabela oficial do Ministério do Trabalho e Emprego que identifica e padroniza as ocupações do mercado de trabalho brasileiro. Cada ocupação tem um código de seis dígitos e uma descrição.

No Pessoas+, a tela **CBO** permite cadastrar as ocupações utilizadas pela empresa. Depois de cadastrada, a CBO é vinculada ao **cargo** ou à **função**, conforme a parametrização da empresa. Assim, todos os colaboradores daquele cargo ou função passam a ter a mesma classificação ocupacional.

A CBO é utilizada principalmente:

- no envio das informações do trabalhador ao eSocial, como no evento de admissão (S-2200);
- na definição do tipo de horário noturno (urbano ou rural) considerado no cálculo da Folha de Pagamento;
- em documentos e obrigações que exibem a ocupação do colaborador, como o recibo de pagamento (holerite).

### Antes de começar

- Tenha acesso liberado à tela **CBO**. A liberação é feita pelo administrador do sistema na tela **Acessos** (Configurações > Controle de Acesso).
- Consulte o código e a descrição da ocupação na tabela oficial da CBO.
- Defina se a CBO será informada no cargo ou na função, no parâmetro **Onde Utiliza o CBO? - FPUTILIZACBO**.

### Jornada de uso

#### 1. Cadastrar a CBO

![Imagem 1: 1. Cadastrar a CBO](https://ajuda.sankhya.com.br/hc/article_attachments/41400748699927)

O cadastro registra a ocupação no sistema para que ela possa ser vinculada aos cargos ou às funções da empresa.

1. Acesse a tela **CBO** (Pessoal+ > Cadastros).
2. Clique em + **Cadastrar CBO**.
3. No campo **Código**, informe o código da ocupação conforme a tabela oficial. O campo aceita até seis dígitos.
4. No campo **Descrição**, informe a descrição da ocupação.
5. Salve o cadastro, se necessário, para concluir a inclusão.

| **💡 Dica**  Utilize o código e a descrição exatamente como aparecem na tabela oficial. Isso facilita a conferência das informações enviadas ao eSocial e a consulta em auditorias. |
| --- |

Após o cadastro, a CBO fica disponível para ser vinculada aos cargos ou às funções.

#### 2. Configurar o tipo do horário noturno

O campo **Tipo do Horário Noturno**, disponível na aba **Geral**, define o tipo de horário noturno associado à CBO.

Selecione a opção adequada:

- **Urbano:** para trabalhadores urbanos;
- **Rural (Lavoura):** para trabalhadores rurais que atuam em atividades agrícolas;
- **Rural (Pecuária):** para trabalhadores rurais que atuam em atividades pecuárias.

Depois de selecionar a opção, clique em **Salvar (F7)**.

**Regra aplicada:** o tipo de horário noturno definido no sindicato tem prioridade sobre o tipo informado na CBO. Quando a opção **Regra Ad. Noturno** está marcada no sindicato do colaborador, o sistema considera o campo **Tipo Hor. Noturno** informado no sindicato. Caso contrário, considera o tipo definido na CBO vinculada ao cargo ou à função do colaborador.

| **🚨 Risco operacional**  As regras de horário noturno urbano e rural são diferentes. Uma configuração incorreta pode afetar o cálculo do adicional noturno. Antes de utilizar a CBO, confira se o tipo selecionado corresponde à situação do trabalhador e se o sindicato define uma regra própria. |
| --- |

#### 3. Vincular a CBO ao cargo ou à função

A CBO não é informada diretamente no cadastro do colaborador. Sua origem é definida pelo parâmetro **Onde Utiliza o CBO? - FPUTILIZACBO**, disponível na tela **Preferências** (Configurações > Avançado).

Consulte a configuração do parâmetro para identificar onde a CBO deve ser informada:

| Configuração do FPUTILIZACBO | De onde o sistema busca a CBO |
| --- | --- |
| Cargo (padrão) | Do campo **CBO** do cadastro de cargos. |
| Função | Do campo **CBO** do cadastro de funções. |

Para realizar o vínculo:

1. Acesse a tela **Preferências** e confira o valor do parâmetro **FPUTILIZACBO**.
2. Acesse o cadastro de **Cargos** ou de **Funções**, conforme a configuração do parâmetro.
3. No campo **CBO**, informe a CBO cadastrada na etapa 1.
4. Salve o cadastro.

**Regra aplicada:** no envio das informações ao eSocial, o sistema utiliza a CBO do cargo ou da função registrada no histórico do colaborador para o período, de acordo com a configuração do parâmetro FPUTILIZACBO.

| **⚠️ Atenção**  Alterar o parâmetro FPUTILIZACBO muda a origem da CBO utilizada pelo sistema. Antes de fazer essa alteração, confira se todos os cargos ou funções que passarão a ser utilizados possuem a CBO preenchida. |
| --- |

Após o vínculo, a CBO poderá ser utilizada nas informações dos colaboradores associados ao cargo ou à função, conforme a configuração do sistema.

📚 Configure isso em: [Cadastro de Cargos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41423883668119) ou [Cadastro de Funções](https://ajuda.sankhya.com.br/hc/pt-br/articles/41401796198679).

### Pontos de atenção

- **Ocupação exercida:** selecione uma CBO que corresponda à ocupação efetivamente exercida pelo colaborador.
- **Código oficial:** utilize códigos existentes na tabela oficial da CBO. Códigos inexistentes podem provocar rejeições no envio ao eSocial.
- **Origem da CBO:** o parâmetro **FPUTILIZACBO** determina se o sistema busca a CBO do cargo ou da função. Verifique se o cadastro correspondente está preenchido.
- **Regra de horário noturno:** quando o sindicato do colaborador possui a opção **Regra Ad. Noturno** marcada, o sistema considera o tipo de horário noturno configurado no sindicato, em vez do tipo definido na CBO.
- **Alterações cadastrais:** alterar a CBO de um cargo ou de uma função não atualiza automaticamente eventos já enviados ao eSocial nem folhas já calculadas. Avalie a necessidade de recálculo ou retificação conforme o caso.

### Perguntas frequentes

**1. Onde encontro o código correto da CBO?**

Na tabela oficial da Classificação Brasileira de Ocupações, disponível no site do Ministério do Trabalho e Emprego.

**2. Posso cadastrar um código que não existe na tabela oficial?**

Não é recomendado. O eSocial valida o código da CBO e rejeita códigos inexistentes.

**3. Onde informo a CBO do colaborador?**

No cadastro de cargos ou no cadastro de funções, conforme o parâmetro FPUTILIZACBO. A CBO não é informada diretamente no cadastro do colaborador.

**4. Qual a relação entre CBO, cargo e função?**

A CBO é a ocupação oficial. O cargo e a função são cadastros internos da empresa. O parâmetro FPUTILIZACBO define se a CBO fica no cargo (padrão) ou na função.

**5. Quando devo utilizar horário noturno rural?**

Quando a ocupação estiver relacionada a atividades rurais de lavoura ou pecuária, sujeitas às regras de adicional noturno do trabalhador rural. Confira também se o sindicato do colaborador define uma regra própria de adicional noturno, porque ela tem prioridade.

**6. Alterar a CBO afeta cálculos já realizados?**

Não automaticamente. A alteração vale para os próximos processamentos. Se houver folhas calculadas ou eventos já enviados com a CBO anterior, avalie a necessidade de recálculo ou retificação.

**7. Como exibir ou ocultar a descrição da CBO no holerite?**

Consulte o artigo [Descrição do CBO do holerite](https://ajuda.sankhya.com.br/hc/pt-br/articles/39352818299671).
