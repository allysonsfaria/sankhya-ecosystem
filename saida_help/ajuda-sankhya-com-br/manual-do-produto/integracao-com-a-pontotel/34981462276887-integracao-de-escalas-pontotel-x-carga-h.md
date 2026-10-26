---
id: "34981462276887"
titulo: "Integração de Escalas Pontotel x Carga Horária Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:21Z"
rotulos: ["Integração", "Carga Horária", "ID: br.com.sankhya.cadastro.funcionarios", "eSocial", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "ID: br.com.sankhya.rh.CargaHoraria", "Pessoas+", "Escalas"]
---

# Integração de Escalas Pontotel x Carga Horária Sankhya

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Escalas e Carga Horária

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887-Integra%C3%A7%C3%A3o-de-Escalas-Pontotel-x-Carga-Hor%C3%A1ria-Sankhya#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração entre Pontotel e Sankhya permite sincronizar automaticamente escalas de trabalho e cargas horárias dos colaboradores**, eliminando o cadastro manual em ambas as plataformas. 

Ao criar ou atualizar uma escala na Pontotel, ela é integrada e refletida como carga horária no Sankhya Om, facilitando a gestão e garantindo que os dados estejam sempre alinhados para folha de pagamento e obrigações legais (eSocial).

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om.
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).
  - Cadastro das escalas na Pontotel com código, nome e tipo de escala preenchidos.

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/34981497326743)

### 4. Jornada de Uso

**4.1.** O usuário cadastra ou atualiza uma escala na Pontotel, preenchendo código, nome e tipo de escala.

![Imagem 2: 4.1. O usuário cadastra ou atualiza uma escala na Pontotel, preenchendo código, nome e tipo de escala.](https://ajuda.sankhya.com.br/hc/article_attachments/34999541007511)

**4.2.** A escala é integrada automaticamente para o Sankhya Om como carga horária.

![Imagem 3: 4.2. A escala é integrada automaticamente para o Sankhya Om como carga horária.](https://ajuda.sankhya.com.br/hc/article_attachments/35001024061719)

**4.3.** No Sankhya Om, o usuário associa a carga horária desejada ao cadastro do colaborador.

![Imagem 4: 4.3. No Sankhya Om, o usuário associa a carga horária desejada ao cadastro do colaborador.](https://ajuda.sankhya.com.br/hc/article_attachments/35000979266711)

As associações são sincronizadas e refletidas na Pontotel.

**4.4.** Campos integrados: escala (Pontotel) → carga horária (Sankhya)

| **Campo Pontotel** | **Campo Sankhya** | **Descrição** |
| --- | --- | --- |
| Tabela alimentada no Sankhya: TFPCGH | | |
| Código | CODCARGAHOR | É o campo que faz a relação entre as escalas existentes na Pontotel e as cargas horárias existentes na Sankhya. Não deve ser alterado nem na Sankhya, nem na Pontotel para não perder a referência. |
| Nome da escala | DESCRCARGAHOR | Descrição a ser enviada para o esocial. |
| Tipo de escala | TPJORNADA | Opções:   2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)   3 - Jornada com horário diário fixo e folga variável    4 - Jornada com horário diário fixo e folga fixa (no domingo)   5 - Jornada com horário diário fixo e folga fixa (exceto no domingo)   6 - Jornada com hr/diário fixo e folga fixa (outro dia da semana), c/ folga adicional periódica no domingo;   7 - Turno ininterrupto de revezamento;   9 - Demais tipos de jornada. |

### 5. Pontos de Atenção

- O campo "código" da escala é o vínculo entre Pontotel e Sankhya. Não altere após o cadastro.
- O tipo de escala é obrigatório para integração e reporte ao eSocial.
- Se houver uma escala na Pontotel com o mesmo código de uma carga horária já existente no Sankhya Om, os dados serão atualizados conforme a Pontotel.
- Se uma escala for excluída na Pontotel, deverá ser excluída manualmente no Sankhya Om. Se for excluída direto no Sankhya Om, será reintegrada pela Pontotel, uma vez que a origem da informação das escalas existentes é a Pontotel.
- As alterações que não sensibilizem o log de alterações no Sankhya Om só integram na execução de consistência diária.

### 6. Dicas de Usabilidade

- Sempre preencher o tipo de escala nas configurações avançadas da Pontotel.
- Manter o código da escala consistente para garantir a referência entre sistemas.
- Utilizar filtros para localizar escalas e cargas horárias rapidamente.
- Verificar a validade do token e a responsividade da base Sankhya antes de executar integrações.

### 7. Casos de Uso

✅ **Exemplo Real:** 

Cadastro de uma nova escala "6x1 com pausa de 1 hora" na Pontotel, integrada automaticamente como carga horária no Sankhya Om.

❌ **Erro Comum:** 

Cadastro de escala na Pontotel sem preencher o tipo de escala, impedindo a integração com o Sankhya Om.

## FAQ – Dúvidas Frequentes

1. **O que acontece se eu cadastrar uma escala na Pontotel com código já existente no Sankhya?**

   A escala será considerada equivalente e os dados da carga horária no Sankhya serão atualizados conforme a Pontotel.
2. **Posso excluir uma escala na Pontotel e esperar que seja excluída no Sankhya?**

   Não. Exclusões devem ser feitas manualmente em ambas as plataformas.
3. **O que ocorre se o tipo de escala não for preenchido?**

   A escala não será integrada ao Sankhya, pois o tipo é obrigatório para o eSocial.
4. **Como garantir que a integração funcione corretamente?**

   Certifique-se de que o log de alterações está habilitado, o token está válido e a base Sankhya está online.

## Artigos Relacionados

- [Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118373)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
