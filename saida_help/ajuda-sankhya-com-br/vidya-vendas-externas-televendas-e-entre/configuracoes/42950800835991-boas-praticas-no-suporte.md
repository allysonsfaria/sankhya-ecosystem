---
id: "42950800835991"
titulo: "Boas práticas no suporte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950800835991-Boas-pr%C3%A1ticas-no-suporte"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:11:53Z"
rotulos: ["sync_hc", "vidya", "vidya_600140", "sync_hash_61794ab15a19"]
---

# Boas práticas no suporte

### 1. Mentalidade de atendimento

A primeira boa prática é entender que **suporte não é simplesmente responder tickets**.

O objetivo é:

> **Entender o problema → identificar a causa → orientar corretamente → validar a solução → registrar o conhecimento.**

Alguns princípios importantes:

- Não responder apenas para “tirar o ticket da fila”.
- Não assumir que o problema é um bug antes de investigar.
- Não assumir que o cliente está errado.
- Não assumir que o sistema está errado.
- Sempre tentar entender **o cenário completo**.
- Buscar a causa, e não apenas tratar o sintoma.
- Quando não souber, investigar antes de responder.
- Nunca inventar uma resposta para demonstrar segurança.
- Se precisar escalar, escalar **com contexto e evidências**.

> **“Nosso objetivo não é fechar tickets. É resolver problemas.”**

---

## 2. Boas práticas de comunicação com o cliente

Aqui existe uma diferença importante entre **ser rápido** e **ser eficiente**.

#### Evitar

> “Vou verificar.”

> “É problema do sistema.”

> “Isso é com o Sankhya.”

> “Vou passar para o desenvolvimento.”

Essas respostas não ajudam o cliente a entender o que está acontecendo.

#### Preferir

> “Vou analisar o comportamento apresentado comparando o cenário no aplicativo com as informações do ERP. Assim consigo identificar se estamos diante de uma configuração, integração ou comportamento do produto.”

Isso demonstra **processo e domínio técnico**.

#### Regra importante

Sempre que possível, a comunicação deve responder três perguntas:

**1. O que identificamos?**
**2. O que estamos fazendo?**
**3. Qual é o próximo passo?**

Exemplo:

> “Identificamos que o pedido está sendo enviado corretamente pelo aplicativo, porém a informação não está sendo refletida no ERP. Vamos validar agora o retorno da integração para identificar em qual etapa ocorre a divergência.”

Isso reduz muito a ansiedade do cliente.

---

## 3. Nunca pedir informação que já está disponível

Uma das coisas que mais prejudicam a experiência do cliente é fazer o cliente repetir informações.

Antes de perguntar:

> “Qual é o código do pedido?”

verifique se ele já informou isso.

Antes de perguntar:

> “Qual versão do aplicativo?”

verifique se essa informação já está disponível no ticket.

Antes de solicitar novamente um print, vídeo ou evidência, veja se o cliente já enviou.

#### Regra:

**Leia o histórico inteiro antes de responder.**

Principalmente quando o ticket possui várias interações.

---

## 4. Fazer perguntas técnicas, não perguntas genéricas

Uma boa análise começa com perguntas que reduzem o espaço de investigação.

Em vez de:

> “O que está acontecendo?”

Preferir:

> “Esse comportamento ocorre com todos os pedidos ou somente com esse pedido específico?”

ou:

> “O problema ocorre para todos os representantes ou somente para esse usuário?”

ou:

> “O produto possui estoque no local 109001 no ERP?”

Isso transforma o atendimento em uma **investigação estruturada**.

---

## 5. Reproduzir o problema sempre que possível

Uma das melhores práticas de suporte técnico é:

> **Não confiar apenas na descrição do cliente.**

Quando possível:

1. Entender o cenário.
2. Reproduzir.
3. Comparar o resultado esperado com o resultado obtido.
4. Identificar onde ocorre a divergência.
5. Só então definir a causa provável.

Por exemplo:

**Esperado:**
Produto deve utilizar o local 109001.

**Obtido:**
Aplicação utiliza o local 108001.

**Investigação:**

- Qual local está configurado no produto?
- Qual local está configurado na TOP?
- Existe estoque?
- Existe regra de prioridade?
- O ERP retorna o local?
- O aplicativo está sobrescrevendo a informação?
- O comportamento ocorre em outros produtos?

Isso é muito mais eficiente do que simplesmente abrir um bug.

---

## 6. Diferenciar sintoma de causa

Imagine:

> “O pedido não sincroniza.”

Isso é o **sintoma**.

A causa pode ser:

- erro de autenticação;
- falha na API;
- parâmetro;
- cadastro;
- timeout;
- versão do aplicativo;
- erro no ERP;
- inconsistência de dados;
- regra de negócio;
- problema de infraestrutura.

Então o analista não deveria registrar:

> “Pedido não sincroniza.”

E sim algo como:

> “Pedido 12345 não foi sincronizado. Durante a análise, identificamos que a API retorna erro X ao processar o item Y.”

Isso muda completamente a qualidade do suporte.

---

## 7. Diferenciar configuração, operação, integração e bug

#### Configuração

O sistema está funcionando corretamente, mas existe uma configuração inadequada.

#### Operação

O sistema está funcionando conforme projetado, mas o usuário está realizando uma operação diferente da esperada.

#### Dados

Existe alguma inconsistência ou ausência de informação nos cadastros.

#### Integração

O problema ocorre na comunicação entre sistemas.

#### Bug

O comportamento observado é diferente do comportamento especificado/esperado mesmo com configuração e dados corretos.

#### Evolução

O sistema funciona conforme especificado, mas o cliente deseja um novo comportamento.

Isso evita um problema muito comum:

> **Transformar qualquer dificuldade do cliente em bug.**

---

## 8. Antes de escalar para desenvolvimento

Essa é uma das práticas mais importantes para o relacionamento entre **Suporte e Desenvolvimento**.

Um ticket não deveria chegar para desenvolvimento simplesmente assim:

> “Cliente informou que não funciona.”

O desenvolvimento precisa receber um **pacote de investigação**.

Idealmente:

#### Contexto

O que o cliente está tentando fazer?

#### Cenário

Qual cliente, usuário, pedido, produto, operação etc.?

#### Comportamento atual

O que está acontecendo?

#### Comportamento esperado

O que deveria acontecer?

#### Evidências

- prints;
- vídeos;
- logs;
- payload;
- retorno da API;
- SQL;
- IDs;
- horários;
- versão;
- ambiente.

#### Testes realizados

O que o suporte já tentou?

#### Resultado dos testes

O que cada teste apresentou?

#### Conclusão

Por que o suporte acredita que seja um problema de desenvolvimento?

---

## 9. Nunca escalar um problema sem tentar entender a causa

> **“Escalonamento não é transferência de responsabilidade. É continuidade da investigação.”**

Antes de enviar para desenvolvimento, o analista deveria conseguir responder:

**“Por que acredito que isso seja um problema do produto?”**

Se você não consegue responder, provavelmente ainda precisa investigar.

---

## 10. Boas práticas com banco de dados

#### Antes de executar um SELECT:

Entender:

- qual informação está procurando;
- qual tabela provavelmente armazena essa informação;
- qual relacionamento existe;
- qual campo identifica o registro.

#### Ao utilizar SQL:

Preferir consultas controladas e específicas.

Evitar:

```
SELECT *
```

quando não há necessidade.

Preferir:

```
SELECT CODPROD, DESCRPROD, CODLOCALPADRAO
FROM TGFPRO
WHERE CODPROD = 2005;
```

Isso facilita a análise e reduz ruído.

#### Outra boa prática:

Não confiar em apenas uma tabela.

No Sankhya, muitas análises precisam cruzar informações de:

- cabeçalho;
- itens;
- produtos;
- estoque;
- parceiros;
- empresas;
- locais;
- TOP;
- parâmetros;
- configurações.

O analista deve entender **a relação entre as informações**, e não apenas procurar um campo.

---

## 11. Documentar o que descobriu

Se um analista passou 40 minutos investigando determinado comportamento e descobriu a causa, essa informação não deveria morrer dentro daquele ticket.

Perguntas importantes:

> Isso pode acontecer novamente?

> Outro analista poderia receber esse mesmo problema?

> Existe algum conhecimento que deveria entrar na base?

Se sim, documentar.

Isso cria um ciclo:

**Ticket → Investigação → Solução → Conhecimento → Base → Atendimento mais rápido.**

Esse é um dos pontos que mais pode ajudar vocês a reduzir dependência de pessoas específicas.

---

## 12. Não guardar conhecimento “na cabeça”

Isso é particularmente importante para pessoas mais experientes do time.

Se somente uma pessoa sabe:

- determinada configuração;
- determinado SQL;
- determinada regra;
- determinado fluxo;
- determinada integração;

vocês têm um **ponto único de dependência**.

O conhecimento deve sair da pessoa e ir para:

- Base de conhecimento;
- documentação técnica;
- procedimentos;
- artigos;
- exemplos de tickets;
- consultas SQL úteis.

---

## 13. Sempre registrar a solução de forma reproduzível

Uma boa documentação não deveria dizer somente:

> “Foi ajustada a configuração.”

Melhor:

> “Acesse X → localize Y → altere o parâmetro Z → salve → sincronize → valide novamente.”

A diferença é enorme.

A primeira frase informa **o que aconteceu**.

A segunda ensina **como resolver**.

---

## 14. Cuidado com versões

Quando houver comportamento inesperado:

**Verificar:**

- versão do aplicativo;
- versão disponível atualmente;
- versão do backend;
- versão do Manager, quando aplicável;
- se outros usuários apresentam o mesmo comportamento;
- se o problema começou após atualização.

Uma pergunta importante:

> **“Esse problema começou depois de alguma atualização?”**

Pode economizar muito tempo.

---

## 15. Comparar cenários

Uma técnica extremamente poderosa para suporte:

#### Cenário que funciona × cenário que não funciona

Exemplo:

| Informação | Funciona | Não funciona |
| --- | --- | --- |
| Usuário | João | Pedro |
| Produto | 1001 | 1002 |
| Empresa | 1 | 1 |
| TOP | 3101 | 3101 |
| Local | 109001 | 108001 |
| Versão | Atual | Atual |

A diferença entre os cenários frequentemente revela a causa.

---

## 16. Encerramento também faz parte do atendimento

Fechar ticket não significa apenas mudar o status.

Antes de encerrar:

- A solução foi aplicada?
- O cliente conseguiu realizar a operação?
- O comportamento foi normalizado?
- Existe alguma pendência?
- A orientação foi suficientemente clara?

Sempre que possível:

> **Confirmar a resolução antes do encerramento.**

---

## 17. Criar um padrão mínimo de qualidade para todos os tickets

#### Antes de responder

- Li todo o histórico?
- Entendi o problema?
- Sei qual é o comportamento esperado?
- Tenho evidência suficiente?

#### Durante a análise

- Consigo reproduzir?
- Comparei cenário funcionando × não funcionando?
- Validei configuração?
- Validei dados?
- Validei versão?
- Validei integração?
- Consultei a base?

#### Antes de escalar

- Sei por que estou escalando?
- Registrei o que já foi testado?
- Enviei evidências?
- Expliquei comportamento atual × esperado?

#### Antes de encerrar

- O problema foi resolvido?
- O cliente entendeu a solução?
- A solução ficou documentada?
- Esse conhecimento deveria virar artigo?

---

## 18. E talvez o mais importante: cultura de time

#### 1. Ajude o colega

Se você já resolveu aquele problema, compartilhe o caminho.

#### 2. Não esconda conhecimento

Conhecimento compartilhado fortalece o time.

#### 3. Pergunte antes de escalar

Mas também **não fique horas preso sozinho** em algo que precisa de outra área.

#### 4. Questione processos

Se algo gera muitos tickets, talvez o problema não seja o usuário.

#### 5. Observe padrões

Um ticket isolado pode ser problema operacional.
50 tickets semelhantes podem indicar **problema estrutural**.

#### 6. Transforme recorrência em ação

Se o mesmo problema aparece repetidamente:

**Ticket → padrão → causa → ação preventiva.**
