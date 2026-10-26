---
id: "44012189207831"
titulo: "Como configurar os Tributos da Reforma Tributária no Magis5 ERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012189207831-Como-configurar-os-Tributos-da-Reforma-Tribut%C3%A1ria-no-Magis5-ERP"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:04Z"
rotulos: ["sync_hc", "magis5", "sync_hash_e5ebb66501f9", "magis5_204048273494"]
---

# Como configurar os Tributos da Reforma Tributária no Magis5 ERP

## Neste artigo, você vai entender como ajustar corretamente as informações de tributos da nova Reforma Tributária no nosso ERP

---

A funcionalidade de Reforma Tributária no Magis5 ERP visa permitir a emissão de documentos fiscais conforme o novo modelo tributário nacional, contemplando os tributos I**BS (Imposto sobre Bens e Serviços)** e **CBS (Contribuição sobre Bens e Serviços).**

Nesta fase inicial, o sistema já possui a estrutura fiscal necessária, aplicando valor e classificações padronizadas, garantindo aderência ao layout fiscal vigente e evitando rejeições junto à SEFAZ.

### Como ativar o IBS e CBS

Para indicar que deseja enviar as informações da**Reforma Tributária** para as notas fiscais, será necessário ativar a opção **"Enviar Dados da Reforma Tributária?"**Feito login Magis5 ERP, acesse "**Configurações",** "**Configurações Gerais"**. Em seguida, selecione a opção "**Fiscal"** e role a página até "**Configuração de NF-e"**.

![Captura de tela 2026-01-02 150301](https://ajuda.sankhya.com.br/hc/article_attachments/44012235605271)

![Captura de tela 2026-01-02 151902](https://ajuda.sankhya.com.br/hc/article_attachments/44012221696535)

![Imagem 3: Com essa opção "Enviar Dados da Reforma Tributária" ativa preencheremos automaticamente os demais campos exigidos pela…](https://ajuda.sankhya.com.br/hc/article_attachments/44012189490327)

Com essa opção **"Enviar Dados da Reforma Tributária"** ativa preencheremos automaticamente os demais campos exigidos pela Reforma Tributária, aplicando as alíquotas de teste para 2026.

⚠️ **Lembrando que essa opção só deve ser ativa a partir de 2026 ⚠️**

### Onde configurar os tributos da Reforma Tributária (IBS e CBS)

As configurações estão vinculadas às **Regras de Tributo (V2)** e são aplicadas automaticamente durante a emissão da nota fiscal.

Para visualizar as configurações de **IBS** e **CBS**, vá até a aba **"Configurações"** e por fim **"Regra de Tributo V2"

![Imagem 4: Para visualizar as configurações de IBS e CBS , vá até a aba "Configurações" e por fim " Regra de Tributo V2"](https://ajuda.sankhya.com.br/hc/article_attachments/44012249655319)**

Localize a regra desejada na lista e clique no botão **Editar** para visualizar ou alterar as informações.

![Imagem 5: Localize a regra desejada na lista e clique no botão Editar para visualizar ou alterar as informações.](https://ajuda.sankhya.com.br/hc/article_attachments/44012214686487)

Ao editar uma Regra Fiscal, os filtros das operações cadastradas serão exibidos. Para visualizar e configurar os campos de **IBS e CBS**, selecione e edite o filtro correspondente.

![Captura de tela 2025-12-23 180221](https://ajuda.sankhya.com.br/hc/article_attachments/44012214832535)

Navegue até a etapa **IBS e CBS,**é nessa etapa que o sistema apresenta os dados relacionados à Reforma Tributária.

![Imagem 7: Navegue até a etapa IBS e CBS, é nessa etapa que o sistema apresenta os dados relacionados à Reforma Tributária.](https://ajuda.sankhya.com.br/hc/article_attachments/44012214912791)

### Configuração de IBS e CBS

Na etapa **IBS e CBS**, estão disponíveis os campos abaixo para o detalhamento da carga tributária.

- **CST IBS/CBS:** Define o Código de Situação Tributária que identifica a tributação do imposto
- **Código de Classificação Tributária (cClassTrib):** Campo destinado à classificação da mercadoria ou serviço conforme a tabela oficial da Receita Federal.
- **Alíquota do IBS na UF (%):** Percentual referente ao Imposto sobre Bens e Serviços, destinado ao Estado e Município de destino.
- **Alíquota do CBS (%):** Percentual referente à Contribuição sobre Bens e Serviços, destinada à União (âmbito federal).

**Estes campos estão estruturados conforme as normas nacionais e o layout fiscal vigente, garantindo a correta transmissão dos dados da Reforma Tributária.**

Atualmente **Magis5 ERP** aplica automaticamente os valores padrões estabelecidos para a fase de transição da Reforma Tributária.

- **CST** IBS/CBS:
  000  Tributação integral - Utilizado para operações com incidência total dos novos impostos.
- **Código de Classificação Tributária (cClassTrib):**

  000001  Situações tributadas integralmente pelo IBS e CBS - Identifica situações tributadas integralmente pelo IBS e CBS
- **Alíquota do IBS na UF:**

  **0,1% -** Alíquota de teste/transição destinada aos Estados e Municípios.
- **Alíquota do CBS:**
  **0,9% -** Alíquota de teste/transição destinada à União (Federal).

![Captura de tela 2025-12-23 181231](https://ajuda.sankhya.com.br/hc/article_attachments/44012250048791)

⚠️ **Nota Importante:** No momento, os campos de **IBS e CBS** estão configurados apenas para leitura e bloqueados para edição manual. Essa medida garante que os cálculos permaneçam em conformidade com as alíquotas oficiais da fase de transição estabelecidas pelo Governo Federal.
