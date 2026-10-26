---
id: "42521124311575"
titulo: "Bloqueio do cálculo de férias para colaboradores afastados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42521124311575-Bloqueio-do-c%C3%A1lculo-de-f%C3%A9rias-para-colaboradores-afastados"
trilha: "Manual do Produto > Pessoas+ > Férias > Cálculo de Férias"
atualizado_em: "2026-09-27T18:04:19Z"
rotulos: ["Férias", "Cálculo de Férias", "Quitação de Férias em caso de Afastamento"]
---

# Bloqueio do cálculo de férias para colaboradores afastados

**Módulo:** Pessoal+
**Versão Mínima:**5.115
**Caminho de Acesso:**Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.CalculoIndFolha

---

### Descrição e Usabilidade

O Pessoal+ impede o cálculo de férias quando o período de gozo informado coincide com um afastamento incompatível com férias, conforme as regras da legislação trabalhista e da Tabela 18 do eSocial.

Essa validação é aplicada automaticamente pelo sistema e não pode ser desabilitada por configuração ou parâmetro.

| **⚠️** **Atenção**  Essa regra atua apenas durante o cálculo das férias. O cadastro e a manutenção dos afastamentos continuam sendo realizados normalmente pela rotina de Ocorrências (Pessoal+ > Rotinas Folha). |
| --- |

O cálculo de férias é bloqueado quando existir um afastamento incompatível que coincida com o período de gozo das férias.

O sistema considera duas situações:

| Situação do afastamento | Comportamento |
| --- | --- |
| Com data de término | O bloqueio ocorre quando qualquer dia do afastamento coincide com o período das férias. |
| Sem data de término | O afastamento é considerado em andamento e o cálculo é bloqueado sempre que sua data de início for anterior ao término das férias. |

O bloqueio é aplicado para os seguintes motivos de afastamento previstos na **Tabela 18 do eSocial**:

| Código | Motivo |
| --- | --- |
| 01 | Acidente ou doença do trabalho |
| 03 | Acidente ou doença não relacionada ao trabalho |
| 06 | Aposentadoria por invalidez |
| 11 | Cárcere |
| 17, 18 e 35 | Licença-maternidade e prorrogações |
| 21 | Licença não remunerada |
| 27, 41 e 42 | Qualificação (suspensão contratual) |
| 29 | Serviço militar obrigatório |

#### Como o bloqueio funciona

- **Cálculo individual**

  Após inserir os dados e clicar em **Calcular** as férias, o sistema verifica se existe um afastamento incompatível durante o período informado.

  Caso exista, o cálculo não é realizado e é exibida uma mensagem de bloqueio com o motivo correspondente:

  **"Cálculo de férias bloqueado. Funcionário em afastamento: [Código] – [Descrição do motivo]"**

  [GIF animado: Imagem 1: "Cálculo de férias bloqueado. Funcionário em afastamento: (Código) – (Descrição do motivo)"](https://ajuda.sankhya.com.br/hc/article_attachments/42526588950295)
- **Cálculo coletivo**

  O sistema processa normalmente os colaboradores selecionados.

  Ao conferir o resultado do cálculo no **Gerenciador de Folhas**, quando houver colaboradores com afastamento incompatível, o sistema:

  - não gera a folha de férias dos colaboradores;
  - registra uma **Advertência** informando que o cálculo foi bloqueado;
  - permite consultar os colaboradores afetados ao selecionar o registro da advertência.

  [GIF animado: Imagem 2: permite consultar os colaboradores afetados ao selecionar o registro da advertência.](https://ajuda.sankhya.com.br/hc/article_attachments/42527084249751)

Quando a mensagem for apresentada:

1. verifique as datas do afastamento cadastradas na tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. caso o afastamento tenha sido informado incorretamente, ajuste as datas ou informe a data de término;
3. se o afastamento estiver correto e ainda em andamento, reagende o período de férias ou aguarde o encerramento do afastamento para realizar o cálculo.

Esta validação não interfere nas seguintes situações:

- cadastro de afastamentos durante um período de férias já iniciado;
- manutenção das ocorrências do colaborador;
- regra de quitação de férias em afastamentos prolongados.

📚Para informações sobre afastamentos superiores a 180 dias, consulte o artigo [**Quitação de Férias em caso de Afastamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151).

### Pontos de Atenção

- No cálculo individual, o bloqueio impede o processamento das férias do colaborador.
- No cálculo coletivo, o processamento do lote é concluído normalmente. Os colaboradores impedidos são informados por meio de uma advertência no **Gerenciador de Folhas** e não têm a folha de férias gerada.
- Não existe parâmetro ou configuração para desabilitar essa validação.
- O cálculo das férias somente poderá ser realizado após a correção das datas do afastamento ou a definição de um período de férias que não coincida com ele.

### Perguntas Frequentes (FAQ)

**1. Posso calcular férias mesmo com um afastamento incompatível?**

Não. Enquanto houver sobreposição entre o afastamento e o período de férias, o cálculo permanecerá bloqueado.

**2. Existe algum parâmetro para desativar essa validação?**

Não. Essa é uma regra fixa do sistema.

**3. O bloqueio impede cadastrar um afastamento durante as férias?**

Não. A validação atua apenas no cálculo das férias.

**4. O bloqueio substitui a regra de quitação de férias por afastamento superior a 180 dias?**

Não. São regras independentes.

**5. O cálculo coletivo é interrompido quando existe um colaborador com afastamento incompatível?**

Não. Os colaboradores com afastamento incompatível não têm a folha de férias gerada e são apresentados em uma **Advertência** no **Gerenciador de Folhas**, onde é possível consultar os registros bloqueados.

**6. Como liberar novamente o cálculo de férias?**

Corrija o cadastro do afastamento, informe sua data de término quando aplicável ou reprograme as férias para um período sem sobreposição.
