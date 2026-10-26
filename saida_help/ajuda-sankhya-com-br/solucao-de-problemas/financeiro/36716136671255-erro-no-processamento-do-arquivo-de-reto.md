---
id: "36716136671255"
titulo: "Erro no processamento do arquivo de retorno: (Arquivo ou diretório não encontrado)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36716136671255-Erro-no-processamento-do-arquivo-de-retorno-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:22:29Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "Processamento do Arquivo de Retorno", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Arquivo ou diretório não encontrado", "Erro", "Erro no processamento do arquivo de retorno", "PERMANTPROCRET", "Período p/ manter log de processamento de retorno", "Processamento de Retorno"]
---

# Erro no processamento do arquivo de retorno: (Arquivo ou diretório não encontrado)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36716136663319) **MENSAGEM:**

(Arquivo ou diretório não encontrado)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36716136666903)SOLUÇÃO:**

#### Limpeza de Arquivos Temporários

**(1)** Exclua arquivos temporários.

**(2)** Essa ação deve ser realizada pela **equipe de TI da empresa** ou pelo **responsável pelo Banco de Dados**.

#### Configuração do parâmetro

A limpeza automática dos registros de Log de Processamento de Retorno depende da configuração do parâmetro, pois ambos atuam como uma única validação.

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** pesquise pelo parâmetro ''**PERMANTPROCRET - “Período p/ manter log de processamento de retorno''**.

**(3)** Defina, em dias, o período pelo qual o sistema manterá o histórico dos arquivos processados.

#### Configuração na Tela de Processamento de Retorno

**(1)** Acesse a tela [''**Processamento do Arquivo de Retorno''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno) (Financeiro » EDI Bancário » Processamento do Arquivo de Retorno).

**(2)** Na aba **''Preferências''**, verifique se a opção **''Manter automaticamente apenas os registros mais recentes''** está ativada.

**(3)** Essa opção funciona em conjunto com o parâmetro ''PERMANTPROCRET'', determinando **quando** e **como** os registros serão removidos.

![Imagem 3: (3) Essa opção funciona em conjunto com o parâmetro ''PERMANTPROCRET'' , determinando quando e como os registros serão…](https://ajuda.sankhya.com.br/hc/article_attachments/36716136667671)

#### Funcionamento da limpeza durante o processamento

Quando o sistema identificar a necessidade de limpeza dos registros, é exibido um pop-up de **''Aviso''**, apresentando três possibilidades de ação.

Opções exibidas no aviso:

1. **Remover os registros mais antigos** (Altamente recomendável)
   1.1 **Manter automaticamente apenas os registros mais recentes** (subopção da opção 1)
2. **Não remover** (Pode causar lentidão em curto prazo)

##### Como cada opção funciona?

##### 1. Apenas a opção ''Remover os registros mais antigos'' marcada

- O sistema executa a limpeza imediatamente.
- Os registros antigos são excluídos conforme o período definido no parâmetro ''PERMANTPROCRET''.
- Quando o log voltar a atingir o limite, o sistema exibirá o aviso novamente para nova confirmação.

**2. Opção ''Remover os registros mais antigos'' + subopção “Manter automaticamente apenas os registros mais recentes” marcadas**

- A limpeza é feita imediatamente.
- A partir desse momento, futuras limpezas ocorrerão **automaticamente**, sem necessidade de exibir o pop-up ou solicitar confirmação do usuário.

**3. Opção “Não remover” marcada**

- Nenhuma limpeza é realizada.
- O acúmulo de registros pode causar **lentidão** e até **erro** na rotina de processamento em curto prazo.

![Imagem 4: O acúmulo de registros pode causar lentidão e até erro na rotina de processamento em curto prazo.](https://ajuda.sankhya.com.br/hc/article_attachments/36716136667927)

**OBSERVAÇÃO:**

As escolhas feitas no pop-up ''Aviso'' impactam diretamente as preferências da tela.

Essas configurações, incluindo as opções de limpeza, são salvas por **usuário**, ou seja, cada usuário pode possuir preferências diferentes.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36716151370775)CAUSA:**

O erro ocorre quando não há espaço suficiente para armazenar novos arquivos processados, impedindo a continuidade da rotina.
