---
id: "4404582004759"
titulo: "Condições de Apresentação de Campos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:30Z"
rotulos: ["Campos", "Configuração", "sankhyaflow", "Condições de Apresentação de Campos", "Mostra apenas campos necessários para melhor usabilidade", "Condição de apresentação de campos", "Define campos exibidos com base em dados preenchidos", "Formulário", "Modelagem"]
---

# Condições de Apresentação de Campos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313285898775) Versão: a partir da 4.7
```

---

Esse é um recurso existente em configurações avançadas de campos, que permite ao modelador condicionar os campos que serão exibidos no formulário em virtude de um determinado dado preenchido em outro campo ou outra regra definida no script de condição de apresentação.

Sendo assim, esse recurso será utilizado quando houver a necessidade dos campos serem apresentados para preenchimento devido a um determinado dado preenchido anteriormente em outro campo do formulário e, dessa forma, o executor de tarefas terá uma melhor experiência de uso do sistema, pois irá visualizar apenas os campos que são realmente requeridos.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#casodeuso)
2. [Configurando a condição de apresentação de campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#configurandoacondi%C3%A7%C3%A3odeapresenta%C3%A7%C3%A3odecampos)
3. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#resultados)

---

#### Caso de Uso

No processo de [Cadastro de Clientes](https://drive.google.com/file/d/1Niouu_at4ps-8Y-rAm3bXrov9tQqLIT_/view), na abertura do processo, o solicitante do cadastro deve preencher os dados gerais do cadastro do cliente. Utilizando o recurso de condição de apresentação de campos, iremos definir que, quando for informado o tipo de cliente, serão exibidos campos específicos para o tipo pessoa física ou tipo pessoa jurídica.

Com isso, iremos visualizar apenas os campos que realmente são de preenchimento necessário para um desses tipos, o que deixa os campos do formulário mais concisos e diminui a possiblidade de preenchimento desnecessário dos mesmos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#top)

#### Configurando a condição de apresentação de campos

Em nosso exemplo, iremos condicionar a apresentação dos campos **"Sexo"**, **"Razão social"**, **"Inscrição Estadual"** e **"Insc. Estadual na UF"** em função do dado preenchido no campo **"Tipo de pessoa"**.

Então, caso o campo Tipo de pessoa seja preenchido com a opção **"Pessoa física"**, o campo Sexo será apresentado para preenchimento e os demais campos serão ocultados do formulário.

De outra forma, sendo selecionada a opção **"Pessoa jurídica"** no campo Tipo de pessoa, ocorrerá o inverso, ou seja, o campo Sexo será ocultado do formulário e os demais serão exibidos para preenchimento.

Em nosso caso de uso, estamos utilizando o formulário do tipo nativo para configurar a condição de apresentação de um campo. Para isso, basta acessar as configurações do formulário através do botão :

[GIF animado: Imagem 2: Em nosso caso de uso, estamos utilizando o formulário do tipo nativo para configurar a condição de apresentação de um…](https://ajuda.sankhya.com.br/hc/article_attachments/4404627146775)

| **Representação do Processo** |
| --- |

Em seguida, devemos selecionar o campo que irá condicionar a apresentação e clicar no botão **"Configurações avançadas de campo"**.

[GIF animado: Imagem 3: Em seguida, devemos selecionar o campo que irá condicionar a apresentação e clicar no botão "Configurações avançadas de…](https://ajuda.sankhya.com.br/hc/article_attachments/4404619922455)

| **Configurações avançadas de campos** |
| --- |

Na sequência, acessamos a aba **"Condição de apresentação"** e definimos a condição de apresentação para o campo Sexo. Após isso, realizamos o mesmo procedimento para os demais campos que terão a apresentação condicionada:

![Imagem 4: Na sequência, acessamos a aba "Condição de apresentação" e definimos a condição de apresentação para o campo Sexo .…](https://ajuda.sankhya.com.br/hc/article_attachments/4404627586839)

| **Script de condição de apresentação de campos** |
| --- |

**Script:**

| ``` // Retorna campo 'Sexo' se campo 'Tipo de Pessoa' for igual a pessoa física (F) return getCampo("TIPPESSOA") == "F"; ``` |
| --- |

**Outra forma de escrever o script seria:**

| ``` // Retorna campo 'Sexo' se campo 'Tipo de Pessoa' for igual a pessoa física (F) var tipoPessoa = getCampo("TIPPESSOA"); if (tipoPessoa == "F") { return true; } else { return false; } ``` |
| --- |

**Observação:** outros métodos de consulta também podem ser utilizados em scripts para condicionar a apresentação de campos, conforme a imagem abaixo:

![Imagem 5: Observação: outros métodos de consulta também podem ser utilizados em scripts para condicionar a apresentação de…](https://ajuda.sankhya.com.br/hc/article_attachments/4404620290455)

| **Funções de Consultas para condicionar a apresentação de campos** |
| --- |

Na imagem abaixo, note que, ao configurar uma condição de apresentação na grade de campos, é apresentado o símbolo ![Imagem 6: Na imagem abaixo, note que, ao configurar uma condição de apresentação na grade de campos, é apresentado o símbolo que…](https://ajuda.sankhya.com.br/hc/article_attachments/4404620341143) que sinaliza essa configuração:

![Imagem 7: Na imagem abaixo, note que, ao configurar uma condição de apresentação na grade de campos, é apresentado o símbolo que…](https://ajuda.sankhya.com.br/hc/article_attachments/4404620320791)

| **Ícone que possui condição de apresentação** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#top)

#### Resultados

Realizadas as configurações de condições de apresentações no ambiente de modelagem, agora podemos visualizar na [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595434-Lista-de-Tarefas) o resultado dessas configurações.

Para isso, acesse o processo configurado e selecione no campo **"Tipo de pessoa"** uma das opções. Assim, é possível visualizar campos que são apresentados quando selecionamos o tipo Pessoa Física:

![Imagem 8: Para isso, acesse o processo configurado e selecione no campo "Tipo de pessoa" uma das opções. Assim, é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/4404627767831)

| **Formulário na Lista de Tarefas - Pessoa Física** |
| --- |

E os campos exibidos quando selecionado o tipo Pessoa Jurídica:

![Imagem 9: E os campos exibidos quando selecionado o tipo Pessoa Jurídica :](https://ajuda.sankhya.com.br/hc/article_attachments/4404627774999)

| **Formulário na Lista de Tarefas - Pessoa Jurídica** |
| --- |

Dessa forma, foram apresentados apenas os campos necessários para preenchimento para cada tipo, o que torna a visualização de campos do formulário mais enxuta e melhora a experiência para os executores de tarefas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404582004759-Condi%C3%A7%C3%B5es-de-Apresenta%C3%A7%C3%A3o-de-Campos#top)
