---
id: "37497561502231"
titulo: "Relatório S-5012 (IRRF consolidado por contribuinte)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Nova DIRF e Informe de Rendimentos > Conferência do IRRF no eSocial"
atualizado_em: "2026-09-27T18:57:29Z"
rotulos: ["Conferência", "Relatórios", "Impostos", "eSocial", "Pessoal+", "IRRF", "ID: br.com.sankhya.mgepes.rh.DashEsocial5012"]
---

# Relatório S-5012 (IRRF consolidado por contribuinte)

**Módulo:** Pessoal+
**Versão Mínima:**5.77.0 
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.DashEsocial5012

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KEC4K3C9EYZTBE00SH6S2RQG)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KEC4TPWJWJWRY3S9XHWY5RW7)

[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KEC57D5Y6GN0EJ087DWMPF57)

[3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KEC5K7VZ1ZCPSX796HWDDQBB)

[Primeiro nível do Dash S-5012](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KECA2S0MY866WQHBQ557M7HQ)

[Segundo nível do Dash S-5012](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KEC1TVPKDKRRP1YMV1CTBB1S)

[4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KECFCFR051VHDMZPMSMJ0E4S)

[5. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KECFCFR5KJVHWZNJQSYNT2FF)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#h_01KECFCFRD2R74ZR2VH84NTSEA)

---

## Descrição e Usabilidade

######

O **Dashboard S-5012 – Informações do IRRF consolidadas por contribuinte** auxilia na **conferência dos valores de Imposto de Renda Retido na Fonte (IRRF)** apurados pelo sistema e aqueles **retornados pelo eSocial**, após o fechamento da folha.

O dashboard permite:

- Visualizar os valores de IRRF **consolidados por Código de Receita (CR)**;
- Comparar os valores **apurados no sistema** com os valores **retornados pelo eSocial**;
- Identificar rapidamente **diferenças ou inconsistências**;
- Navegar para um **segundo nível de detalhamento**, com totalizadores de rendimentos, deduções, isenções e retenções que pode ser usado para conferir com extrator disponibilizado pela Receita.

### 1. Descrição da Funcionalidade

######

O Dash S-5012 consolida dados de **duas origens independentes**:

#### **(1)** Origem eSocial

Utiliza os retornos dos eventos:

- **S-1299** – Fechamento dos eventos periódicos;

  - **S-5012** – Consolidação do IRRF por Código de Receita.
- **S-1210** – Informações de pagamentos.

  - **S-5002** – Bases de cálculo por trabalhador.

#### **(1)** Origem Sistema

Utiliza dados da folha de pagamento, considerando:

- Datas de pagamento;
- Tipos de folha (mensal, férias, rescisão, 13º, PLR, entre outros);
- Configurações dos eventos de folha.

**Regras importantes**

- Os dados **não dependem uma base da outra** para serem exibidos.
- Se existir valor apenas no **Sistema** ou apenas no **eSocial**, o Código de Receita será exibido normalmente, com **indicação de possível divergência**.

### 2. Pré-requisitos

######

#### Permissões necessárias

Para utilizar o dashboard S-5012, é necessário:

- Acesso liberado para a tela **S-5012 – Informações do IRRF consolidadas por contribuinte**.

  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Nota:** o dashboard **será liberado automaticamente para usuário DP** com acesso ativo as telas de Configuração Funcionários, Gerenciador de Folhas e Central do eSocial.

#### Condições obrigatórias

1. Folhas com **data de pagamento** dentro do período informado;
2. Eventos do eSocial devidamente **fechados (S-1299)**;
3. Retornos do **S-5012** processados.

### 3. Jornada de Uso

######

**(1)** O dashboard **S-5012 – Informações do IRRF consolidadas por contribuinte** (Pessoal+ > Consultas) pode ser acessado de duas maneiras:

1. Pela barra de pesquisa do Sankhya Om;

   ![Imagem 1: Pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/37781115628439)
2. Pela **Central do eSocial** (Pessoal+ > Rotinas Folha), clicando no menu **Conferência de Tributos** ou no botão de **mesmo nome**, localizado no canto inferior direito da tela.

   [GIF animado: Imagem 2: Pela Central do eSocial (Pessoal+ > Rotinas Folha), clicando no menu Conferência de Tributos ou no botão de mesmo nome…](https://ajuda.sankhya.com.br/hc/article_attachments/37856515456279)

**(2)** Antes de analisar os dados, informe os filtros obrigatórios:

- **Empresa Matriz**
  - define a empresa responsável pelo envio ao eSocial;
  - a consolidação considera automaticamente **matriz + filiais vinculadas**.
- **Referência de apuração:** escolha entre:
  - **Período Mensal**
    Exemplo: 01/11/2025 a 30/11/2025 ➜ Considera apenas dados do mesmo mês.
  - **Período Anual**
    Exemplo: 01/01/2025 a 31/12/2025 ➜ Considera todas as competências do ano.

🔒 O sistema valida automaticamente o período informado, não permitindo intervalos maiores que um mês ou que ultrapassem a virada de ano.

**(3)** Clique em **Atualizar**.

[GIF animado: Imagem 3: (3) Clique em Atualizar .](https://ajuda.sankhya.com.br/hc/article_attachments/37778548055831)

######

#### Primeiro nível do Dash S-5012

######

**(4)** Analise a **primeira tabela** que exibe o **IRRF retido por Código de Receita (CR)**.

Exemplos de Código de Receita:

- **056107** – IRRF mensal, férias e 13º salário;
- **058806** – IRRF sem vínculo empregatício;
- **356201** – IRRF sobre PLR;
- **188901** – Rendimentos Recebidos Acumuladamente (RRA).
- **056111** – IRRF – Empregado/Trabalhador rural Segurado especial
- **056112** – IRRF – Empregado/Trabalhador rural Segurado especial – 13° salário
- **056113** – IRRF – Empregado/Trabalhador rural Segurado especial – 13° salário rescisório
- **061001** – IRRF sobre serviços de transporte rodoviário internacional de carga pagos a transportador autônomo residente no Paraguai
- **047301** – IRRF – Residentes no exterior

O **CR** será exibido sempre que houver valor em **pelo menos uma das origens** (Sistema ou eSocial).

|  | **Valor do CR eSocial** | **Valor do CR Sistema** | **Diferença** |
| --- | --- | --- | --- |
| **Descrição** | Representa o valor **consolidado pelo eSocial**; após o envio do **S-1299**, o eSocial traz o **retorno** do **S-5012** com a **consolidação** por **Código de Receita**.  **Fonte dos dados:**   - Grupo infoCRMen → tag vrCRMen (IRRF mensal); - **Exceção**: **CR 047301**, que utiliza infoCRDia → vrCRDia. | Representa o valor **apurado internamente pelo sistema**, com base nas folhas com data de pagamento dentro do período selecionado no filtro.  **Considera:**   - Data de pagamento dentro do período selecionado; - Tipos de folha válidos (mensal, férias, rescisão, 13º, PLR, rescisão complementar, dissídio, adiantamento); - Configurações dos eventos (identificação do evento, natureza da rubrica, incidência de IRRF, base de rendimento DIRF). | Exibe a diferença entre os valores:  **Diferença = Valor do CR eSocial – Valor do CR Sistema**  **Regras importantes:**   - Valores nulos são tratados como zero; - Pode resultar em:   - Valor positivo → eSocial maior;   - Valor negativo → Sistema maior;   - Zero → valores iguais. |
| **Em caso de divergência, verifique:** | - Se o fechamento (S-1299) foi realizado corretamente; - Se o período de apuração (perApur) está dentro do filtro; - Se houve reprocessamento ou retificação no eSocial. | - Data de pagamento fora do período; - Evento configurado com incidência incorreta de IRRF; - Evento não vinculado corretamente à folha; - Categoria do trabalhador incompatível com o CR. |

**(5)** A **segunda tabela** apresenta informações **exclusivamente relacionadas a deduções e reembolso de plano de saúde**, separadas por tipo.

![Imagem 4: (5) A segunda tabela apresenta informações exclusivamente relacionadas a deduções e reembolso de plano de saúde ,…](https://ajuda.sankhya.com.br/hc/article_attachments/37778636945175)

- Plano de saúde – Titular;
- Plano de saúde – Dependente;
- Reembolso – Titular;
- Reembolso – Dependente.

|  | **Valor eSocial** | **Valor Sistema** | **Diferença** |
| --- | --- | --- | --- |
| **Descrição** | - Obtido do evento **S-1210** no **retorno** do **S-5002.** - Considera apenas as tags específicas de saúde e reembolso de acordo com layout do eSocial.   - Plano de saúde – Titular - tag no retorno **vlrSaudeTit**   - Plano de saúde – Dependente  - tag no retorno **vlrSaudeDep**   - Reembolso – Titular  - tags no retorno **vlrReemb + vlrReembAnt** presente no **grupo detReembTit**   - Reembolso – Dependente  - tags no retorno **vlrReemb + vlrReembAnt** presente no **grupo detReembDep** | - Baseado na **data de pagamento;** - Considera apenas eventos para **Plano de saúde – Titular**   - Com base DIRF = **Y = Plano de Saúde**   - Com incidência correta de IRRF **67 ou 09.**   - Com natureza de rubrica **9219** para plano médico.   - Na folha a Sequência do **titular = 0** - Considera apenas eventos para **Plano de saúde – Dependente**   - Com base DIRF = **Y = Plano de Saúde**   - Com incidência correta de IRRF **67 ou 09.**   - Com natureza de rubrica **9219** para plano médico.   - Na folha a Sequência do  **dependente** **> 0** - Considera apenas eventos para **Reembolso – Titular**   - Com base DIRF = **Y = Plano de Saúde**   - Com incidência correta de IRRF **67 ou 09.**   - Com natureza de rubrica **1405** para Assistência médica.   - Na folha a Sequência do **titular = 0** e a do  **dependente** **> 0**   - Identificação do evento**: 140-** Reembolso do titular do plano de saúde - Considera apenas eventos para **Reembolso – Dependente**   - Com base DIRF = **Y = Plano de Saúde**   - Com incidência correta de IRRF **67 ou 09.**   - Com natureza de rubrica **1405** para Assistência médica.   - Na folha a Sequência do **titular = 0** e a do  **dependente** **> 0**   - Identificação do evento**:   141 -** Reembolso do dependente Plano Médico | Calculada da mesma forma:  **Diferença = Valor eSocial – Valor Sistema** |

**(6)** **Navegação entre níveis**

Na primeira tabela, ao **clicar duas vezes em um Código de Receita**, o sistema abre o **segundo nível**, detalhando cada [**Tipo de IR no infoIR do S-5002**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#evtIrrfBenef) **de acordo com CR selecionado.**

- Rendimentos tributáveis;
- Deduções da base de cálculo do IRRF;
- Rendimento não tributável ou isento do IRRF;
- Retenções de IRRF;
- Exigibilidade suspensa - Rendimento tributável;
- Exigibilidade suspensa - Retenção do IRRF;
- Exigibilidade suspensa - Dedução da base de cálculo do IRRF;
- Compensação judicial.

#

[GIF animado: Imagem 5: Compensação judicial.](https://ajuda.sankhya.com.br/hc/article_attachments/37778681944983)

#### Segundo nível do Dash S-5012

######

O **segundo nível** é acessado ao **clicar duas vezes sobre um Código de Receita (CR)** exibido no primeiro nível.

Nesse detalhamento, o sistema apresenta os **totalizadores de Rendimentos tributáveis, deduções, isenções e retenções do IRRF, r**ealizando uma comparação entre **eSocial x Sistema** para cada tipo de informação.

######

#### **(1)** CR 056107 – IRRF mensal, férias e 13º salário sobre trabalho assalariado

######

Este Código de Receita contempla **trabalhadores com vínculo empregatício**, exceto segurado especial e empregador doméstico com recolhimento unificado.

- **Categorias de trabalhadores consideradas para CR 056107**

Desde que a **classificação tributária** do **empregador** seja **diferente 22** (Segurado especial, inclusive quando for empregador doméstico).

| **Categoria dos Trabalhadores** | |
| --- | --- |
| 101 | Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT |
| 102 | Empregado - Trabalhador rural por pequeno prazo da Lei 11.718/2008 |
| 103 | Empregado - Aprendiz |
| 105 | Empregado - Contrato a termo firmado nos termos da Lei 9.601/1998 |
| 106 | Trabalhador temporário - Contrato nos termos da Lei 6.019/1974 |
| 107 | Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS |
| 108 | Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS |
| 111 | Empregado - Contrato de trabalho intermitente |
| 301 | Servidor público titular de cargo efetivo, magistrado, ministro de Tribunal de Contas, conselheiro de Tribunal de Contas e membro do Ministério Público |
| 302 | Servidor público ocupante de cargo exclusivo em comissão |
| 303 | Exercente de mandato eletivo |
| 304 | Servidor público exercente de mandato eletivo, inclusive com exercício de cargo em comissão |
| 305 | Servidor público indicado para conselho ou órgão deliberativo, na condição de representante do governo, órgão ou entidade da administração pública |
| 306 | Servidor público contratado por tempo determinado, sujeito a regime administrativo especial definido em lei própria |
| 307 | Militar dos Estados e Distrito Federal |
| 308 | Conscrito |
| 309 | Agente público - Outros |
| 310 | Servidor público eventual |
| 311 | Ministros, juízes, procuradores, promotores ou oficiais de justiça à disposição da Justiça Eleitoral |
| 312 | Auxiliar local |
| 313 | Servidor público exercente de atividade de instrutoria, curso ou concurso, convocado para pareceres técnicos, depoimentos ou audiências no exterior. |
| 314 | Militar das Forças Armadas |
| 401 | Dirigente sindical - Informação prestada pelo sindicato |
| 410 | Trabalhador cedido/exercício em outro órgão/juiz auxiliar - Informação prestada pelo cessionário/dest |
| 501 | Dirigente sindical - Segurado especial |
| 721 | Contribuinte individual - Diretor não empregado, com FGTS |
| 722 | Contribuinte individual - Diretor não empregado, sem FGTS |
| 723 | Contribuinte individual - Empresário, sócio e membro de conselho de administração ou fiscal |
| 761 | Contribuinte individual - Associado eleito para direção de cooperativa, associação ou entidade de classe de qualquer natureza ou finalidade, bem como o síndico ou administrador eleito para exercer atividade de direção condominial, desde que recebam remuneração |
| 901 | Estagiário |
| 902 | Médico residente, residente em área profissional de saúde ou médico em curso de formação |
| 903 | Bolsista |
| 904 | Participante de curso de formação, como etapa de concurso público, sem vínculo de emprego/estatutário |
| 906 | Beneficiário do Programa Nacional de Prestação de Serviço Civil Voluntário |

❌ **Não são considerados os trabalhadores:**

- Segurado especial;
- Trabalhadores sem vínculo;
- Rendimentos classificados como RRA;
- Trabalhadores com residência fiscal no exterior.

#### **(2)**Tipos de IR para CR 056107

######

- **Tipo IR 11 – Remuneração mensal**

O **Tipo IR 11** corresponde aos rendimentos tributáveis pagos ao trabalhador considerando mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de **rendimentos tributáveis** através da tag **vlrRendTrib** grupo **consolidApurMen** no retorno S-5002 para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, **somente entram no cálculo** os eventos que estejam configurados com:   - Base **DIRF = S** – Entra como rendimento tributável; - **Código de incidência de IRRF** igual a **11** ou **13**. |

- **Tipo IR 12 – 13º salário**

 O **Tipo IR 12** corresponde aos rendimentos tributáveis pagos ao trabalhador referentes ao 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de rendimentos tributáveis através da tag **vlrRendTrib13** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = M – 13º Salário; - **Código de incidência de IRRF** igual a **12**. |

- **Tipo IR 31 – Retenção do IRRF sobre Remuneração mensal**

O **Tipo IR 31** corresponde aos valores relativos ao imposto de renda retido na fonte sobre rendimentos do trabalho, mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrCRMen** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = R – IRF sobre rendimentos tributáveis; - **Código de incidência de IRRF** igual a **31 ou 33**. |

- **Tipo IR 32 – Retenção do IRRF sobre 13º salário**

O **Tipo IR 32** corresponde aos valores relativos ao imposto de renda retido na fonte sobre os rendimentos do 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrCR13Men** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = K – IRF sobre rendimentos tributáveis 13; - **Código de incidência de IRRF** igual a **32**. |

- **Tipo IR 41 – Previdência Social Oficial (PSO) – Remuneração mensal**

 O **Tipo IR 41** corresponde aos valores relativos à contribuição previdenciária oficial sobre rendimentos do trabalho, mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrPrevOficial** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = I – Contribuição Previdenciária Oficial; - **Código de incidência de IRRF** igual a **41 ou 43**. |

- **Tipo IR 42 – Previdência Social Oficial (PSO) – 13º salário**

O **Tipo IR 42** corresponde aos valores relativos à contribuição previdenciária oficial sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrPrevOficial13** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** =E – Contribuição Previdenciária Oficial 13º; - **Código de incidência de IRRF** igual a **42**. |

- **Tipo IR 46 – Previdência complementar – Salário mensal**

O **Tipo IR 46** corresponde aos valores de dedução mensal relativos à previdência complementar.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 46**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF**  = H – Previdência privada; - **Código de incidência de IRRF** igual a **46 ou 48**; - **Identificação do evento** = 165 – Evento de Previdência Privada – salário mensal. |

- **Tipo IR 47 – Previdência complementar – 13º salário**

O **Tipo IR 47** corresponde aos valores de dedução relativos à previdência complementar sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 47**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = H – Previdência privada; - **Código de incidência de IRRF** igual a **47**; - **Identificação do evento** = 147 – Evento Previdência Privada 13º. |

- **Tipo IR 61 – FAPI – Remuneração mensal**

O Tipo **IR 61** corresponde aos valores de dedução mensal relativos à previdência complementar FAPI.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 61**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 3 – Rendimentos Tributáveis – Dedução – FAPI; - **Código de incidência de IRRF** igual a **61 ou 66**; - **Identificação do evento** = 152 – Evento FAPI Remuneração Mensal. |

- **Tipo IR 62 – FAPI – 13º salário**

O **Tipo IR 62** corresponde aos valores de dedução relativos à previdência complementar FAPI sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 62**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 3 – Rendimentos Tributáveis – Dedução – FAPI; - **Código de incidência de IRRF** igual a **62**; - **Identificação do evento** = 153 – Evento FAPI 13º. |

- **Tipo IR 63 – Funpresp – Remuneração mensal**

O **Tipo IR 63** corresponde aos valores de dedução mensal relativos à previdência complementar do servidor público.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 63**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard.**  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 4 – Rendimentos Tributáveis – Dedução – Fundo de Servidor Público; - **Código de incidência de IRRF** igual a **63 ou 65**; - **Identificação do evento** = 154 – Evento Funpresp Remuneração Mensal. |

- **Tipo IR 64 – Funpresp – 13º salário**

O **Tipo IR 64** corresponde aos valores de dedução relativos à previdência complementar do servidor público sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 64**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 4 – Rendimentos Tributáveis – Dedução – Fundo de Servidor Público; - **Código de incidência de IRRF** igual a **64**; - **Identificação do evento** = 155 – Evento Funpresp 13º. |

- **Tipo IR 51 – Pensão alimentícia – Remuneração mensal e férias**

O **Tipo IR 51** corresponde aos valores de dedução relativos à pensão alimentícia.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrDedPenAlim**, pertencente ao grupo **penAlim**, com **tpRend = 11 ou 13**, no retorno **S-5002**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = J – Pensão Judicial; - **Código de incidência de IRRF** igual a **51 ou 53**; - **Identificação do evento** = 166 – Evento de Pensão Alimentícia – Remuneração mensal ou 167 – Evento de Pensão Alimentícia – Rescisão. |

- **Tipo IR 52 – Pensão alimentícia – 13º salário**

O **Tipo IR 52** corresponde aos valores de dedução relativos à pensão alimentícia sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrDedPenAlim**, pertencente ao grupo **penAlim**, com **tpRend = 12**, no retorno **S-5002**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = G – Pensão Judicial 13º; - **Código de incidência de IRRF** igual a **52**; - **Identificação do evento** = 168 – Evento de Pensão Alimentícia – 13º salário. |

- **Tipo IR 72 – Diárias**

O **Tipo IR 72** corresponde aos valores relativos a diárias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrDiarias** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = D – Diárias e ajuda de custo; - **Código de incidência de IRRF** igual a **72**; - **Identificação do evento** = 170 – Evento de Diárias. |

- **Tipo IR 73 – Ajuda de Custo**

O **Tipo IR 73** corresponde aos valores relativos à ajuda de custo.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrAjudaCusto** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = D – Diárias e ajuda de custo; - **Código de incidência de IRRF** igual a **73**; - **Identificação do evento** = 157 – Evento Ajuda de Custo. |

- **Tipo IR 74 – Indenização e rescisão de contrato**

O **Tipo IR 74** corresponde aos valores relativos à indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrIndResContrato** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = Z – Inden. Resc. Contrato de trabalho; - **Código de incidência de IRRF** igual a **74**; - **Identificação do evento** = 171 – Evento Indenização e rescisão, inclusive PDV e acidentes de trabalho. |

- **Tipo IR 75 – Abono pecuniário**

O **Tipo IR 75** corresponde aos valores relativos ao abono pecuniário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrAbonoPec** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = W – Abono Pecuniário; - **Código de incidência de IRRF** igual a **75**; - **Identificação do evento** = 172 – Evento de Abono pecuniário. |

- **Tipo IR 700 – Auxílio moradia**

O **Tipo IR 700** corresponde aos valores relativos ao auxílio moradia.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrAuxMoradia** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = D – Diárias e ajuda de custo; - **Código de incidência de IRRF** igual a **700**. |

- **Tipo IR 702 – Bolsa médico residente – Remuneração mensal**

O **Tipo IR 702** corresponde aos valores relativos à bolsa de médico residente.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrBolsaMedico** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 2 – Rendimentos Isentos Bolsa de Médico Residente; - **Código de incidência de IRRF** igual a **702**. |

- **Tipo IR 703 – Bolsa médico residente – 13º salário**

O **Tipo IR 703** corresponde aos valores relativos à bolsa de médico residente sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrBolsaMedico13** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = 2 – Rendimentos Isentos Bolsa de Médico Residente; - **Código de incidência de IRRF** igual a **703**. |

- **Tipo IR 79 – Outras isenções**

O **Tipo IR 79** corresponde aos valores relativos a rendimentos isentos – outros.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores através da tag **vlrIsenOutros** no grupo **consolidApurMen** no retorno **S-5002** para o **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - Base **DIRF** = O – Outros não tributáveis; - **Código de incidência de IRRF** igual a **79**; - **Identificação do evento** = 175 – Evento de Outras isenções. |

- **Tipo IR 7900 – Verbas sem natureza de rendimento, retenção, isenção ou dedução de IR**

O **Tipo IR 7900** corresponde às verbas transitadas pela folha de pagamento de natureza diversa de rendimento, retenção, isenção ou dedução de IR.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Mostra o total de valores retornados pelo evento **S-5002**, considerando o grupo **infoIR** com **tpInfoIR = 7900**, vinculado ao **CR 056107**. | Serão consolidados **apenas os valores dos eventos vinculados à folha** cuja **data de pagamento esteja dentro do período selecionado no dashboard**.  Além disso, somente entram no cálculo os eventos que estejam configurados com:   - **Código de incidência de IRRF** igual a **09**; - **Exceção**: evento de plano de saúde com **natureza de rubrica = 9219**. |

- **Tipo IR 9011 – Exigibilidade suspensa – Rendimento tributável (Remuneração mensal e férias)**

Informações de rendimentos tributáveis com exigibilidade suspensa referentes à remuneração mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, considerando o **CR 056107**, agrupados por empresa Matriz e com data de pagamento dentro do período filtrado. São considerados apenas os valores da **tag vlrRendSusp**, no grupo **infoProcRet / infoValores**, com **indApuracao = 1 (Mensal)**. | Consolida-se, por empresa Matriz, os rendimentos pagos com base na data de pagamento dentro do período informado, quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF = 9011 ou 9013** - Base **DIRF** = **6 – Tributação com exigibilidade suspensa** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9012 – Exigibilidade suspensa – Rendimento tributável (13º salário)**

Informações de rendimentos tributáveis com exigibilidade suspensa referentes ao 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, CR **056107**, por empresa Matriz, considerando a **tag vlrRendSusp**, no grupo **infoProcRet / infoValores**, com **indApuracao = 2 (Anual – 13º)**. | Consolida-se, por empresa Matriz, os rendimentos pagos com base na data de pagamento dentro do período informado, quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF = 9012** - Base **DIRF** = **6 – Tributação com exigibilidade suspensa** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9031 – Exigibilidade suspensa – Retenção do IRRF (Remuneração mensal)**

Valores de IRRF não retidos por decisão administrativa ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrNRetido**, no grupo **infoProcRet / infoValores**, com **indApuracao = 1 (Mensal)**. | Consolidado quando:   - **Código de incidência de IRRF = 9031 ou 9033** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9032 – Exigibilidade suspensa – Retenção do IRRF (13º salário)**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrNRetido**, no grupo **infoProcRet / infoValores**, com **indApuracao = 2 (Anual – 13º)**. | Consolidado quando:   - **Código de incidência de IRRF = 9032** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9831 – Depósito judicial (Mensal)**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrDepJud**, no grupo **infoProcRet / infoValores**, com **indApuracao = 1 (Mensal)**. | Consolidado quando:   - **Código de incidência de IRRF = 9831 ou 9833** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Identificação do evento = 159 – Evento Depósito Judicial** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9832 – Depósito judicial (13º salário)**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrDepJud**, no grupo **infoProcRet / infoValores**, com **indApuracao = indApuracao = 2 (Anual – 13º)**. | Consolidado quando:   - **Código de incidência de IRRF = 9832** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Identificação do evento = 159 – Evento Depósito Judicial** - **Número do Processo (S-5002) = número do processo cadastrado no sistema**, com **IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9041 – Previdência Social Oficial (PSO) – Mensal**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrDedSusp**, no grupo **dedSusp / infoValores**, com:   - **indTpDeducao = 1 (Previdência oficial)** - **indApuracao = 1 (Mensal)** | Consolidado quando:   - **Código de incidência de IRRF = 9041 ou 9043** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - Processo com **INSSTRABALHADOR = ‘S’ ou INSSEMPRESA = ‘S’**, **Abrangência do processo = 3**, **Tipo INSS = 1** - **Evento vinculado ao processo.** |

- **Tipo IR 9042 – PSO – 13º salário**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, CR **056107**, extraídos da **tag vlrDedSusp**, no grupo **dedSusp / infoValores**, com:   - **indTpDeducao = 1 (Previdência oficial)** - **indApuracao = 2 (Anual – 13º)** | Consolidado quando:   - **Código de incidência de IRRF = 9042** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - Processo com **INSSTRABALHADOR = ‘S’ ou INSSEMPRESA = ‘S’**, **Abrangência do processo = 3**, **Tipo INSS = 1** - **Evento vinculado ao processo.** |

- **Tipo IR 9046 – Previdência complementar – Mensal**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDedSusp**, com:   - **indTpDeducao = 2 (Previdência privada)** - **indApuracao = 1 (Mensal)** | Consolidado quando:   - **Código de incidência de IRRF = 9046 ou 9048** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Identificação do evento =  165 –** Evento de Previdência Privada – salário mensal. - **Evento vinculado ao processo.** |

- **Tipo IR 9047 – Previdência complementar – 13º salário**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDedSusp**, com:   - **indTpDeducao = 2 (Previdência privada)** - **indApuracao = indApuracao = 2 (Anual – 13º)** | Consolidado quando:   - **Código de incidência de IRRF = 9047** - Base **DIRF** = **6  Tributação com exigibilidade suspensa** - **Identificação do evento =  147 -** Evento Previdência Privada 13°. - **Evento vinculado ao processo.** |

- **Tipo IR 9051 – Pensão alimentícia – Mensal**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDepenSusp**, no grupo **dedSusp / benefPen**, com:   - **indTpDeducao = 5 (Pensão alimentícia)** - **indApuracao = 1 (Mensal)** | Consolidado quando:   - **Código de incidência de IRRF= 9051 ou 9053** - **Base DIRF = 6  Tributação com exigibilidade suspensa** - **Identificação do evento = 166 -** Evento de Pensão Alimentícia - Remuneração mensal |

- **Tipo IR 9052 – Pensão alimentícia – 13º salário**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDepenSusp**, no grupo **dedSusp / benefPen**, com:   - **indTpDeducao = 5 (Pensão alimentícia)** - **indApuracao = indApuracao = 2 (Anual – 13º)** | Consolidado quando:   - **Código de incidência de IRRF= 9052** - **Base DIRF = 6  Tributação com exigibilidade suspensa** - **Identificação do evento = 168 -** Evento de Pensão Alimentícia - 13° salário° |

- **Tipo IR 9061 – FAPI – Mensal**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDedSusp**, com:   - **indTpDeducao = 3 (FAPI)** - **indApuracao = 1 (Mensal)** | Consolidado quando:   - **Código de incidência de IRRF = 9061 ou 9066** - **Identificação do evento  = 152** - Evento FAPI Remuneração Mensal - **Evento está vinculado ao cadastro da previdência complementar.** |

- **Tipo IR 9062 – FAPI – 13º salário**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrDedSusp**, com:   - **indTpDeducao = 3 (FAPI)** - **indApuracao = indApuracao = 2 (Anual – 13º)** | Consolidado quando:   - **Código de incidência de IRRF = 9062** - **Identificação do evento  = 153 -** Evento FAPI 13° - **Evento está vinculado ao cadastro da previdência complementar.** |

- **Tipo IR 9063 – Funpresp – Mensal**

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Valores do **S-5002**, extraídos da **tag vlrPatrocFunp**, com:   - **indTpDeducao = 4 (Funpresp)** - **indApuracao = 1 (Mensal)** | Consolidado quando:   - **Código de incidência de IRRF = 9063 ou 9065** - **Identificação do evento  = 154 -** Evento Funpresp Remuneração Mensal - **Evento está vinculado ao cadastro da previdência complementar.** |

- **Tipo IR 9064 – Fundação de Previdência Complementar do Servidor Público (Funpresp) – 13º salário**

Informações de valores relacionados à dedução da Funpresp referentes ao 13º salário, com exigibilidade suspensa, em função de processo administrativo ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, considerando o **CR 056107**, agrupados por empresa Matriz e com data de pagamento dentro do período filtrado.  São considerados os valores da **tag vlrPatrocFunp**, no grupo **dedSusp / infoValores**, com:   - **indTpDeducao = 4 (Funpresp)** - **indApuracao = 2 (Anual – 13º salário)** | Consolida-se, por empresa Matriz, os valores pagos com base na data de pagamento dentro do período informado, quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF  = 9064** - **Base DIRF  = 6** – Tributação com exigibilidade suspensa - **Identificação do Evento = 155** – Evento Funpresp 13º - **Número do processo(S-5002) = Número do processo no Sistema** - **Evento vinculado ao processo.** - **Evento vinculado ao cadastro da previdência complementar.** |

- **Tipo IR 9082 – Compensação judicial do ano-calendário**

Informações de valores relacionados à compensação judicial relativa ao ano-calendário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, CR **056107**, agrupados por empresa Matriz e dentro do período selecionado.  São considerados os valores da **tag vlrCmpAnoCal**, no grupo **dedSusp / infoValores**. | Consolida os valores pagos quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF  = 9082** - **Base DIRF  = 6** – Tributação com exigibilidade suspensa - **Identificação do Evento = 160** – Evento Compensação Judicial Ano-Calendário - **Número do processo(S-5002) = Número do processo no Sistema** - **Evento vinculado ao processo.** |

- **Tipo IR 9083 – Compensação judicial de anos anteriores**

Informações de valores relacionados à compensação judicial referente a anos anteriores.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, CR **056107**, agrupados por empresa Matriz e dentro do período selecionado.  São considerados os valores da **tag vlrCmpAnoAnt**, no grupo **dedSusp / infoValores**. | Consolida os valores pagos quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF  = 9083** - **Base DIRF  = 6** – Tributação com exigibilidade suspensa - **Identificação do Evento = 161** – Evento Compensação Judicial Anos Anteriores - **Número do processo (S-5002) = Número do processo no Sistema** - **Evento vinculado ao processo.** |

- **Tipo IR 9067 – Plano privado coletivo de assistência à saúde**

Informações de valores relacionados ao plano de saúde com exigibilidade suspensa, decorrente de processo administrativo ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do **S-5002**, CR **056107**, agrupados por empresa Matriz e dentro do período selecionado.  São considerados os valores do grupo **infoIRComplem / planSaude**, nas **tags vlrSaudeTit** e **vlrSaudeDep**, com:   - **tpInfoIR = 9067** | Consolida os valores pagos quando atendidas todas as condições abaixo:   - **Código de incidência de IRRF  = 9067** - **Natureza da Rubrica = 9219** - **Base DIRF  = 6** – Tributação com exigibilidade suspensa - **Evento vinculado ao plano de saúde.** |

#### **(1)** CR 356201 - IRRF sobre participação dos trabalhadores em lucros ou resultados - PLR

######

Este Código de Receita contempla todo Empregado e Trabalhador Temporário, ou seja, que tenha categoria iniciado em 1xx.

- **Categorias de trabalhadores consideradas para CR 356201**

| **Categoria dos Trabalhadores** | |
| --- | --- |
| 101 | Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT |
| 102 | Empregado - Trabalhador rural por pequeno prazo da Lei 11.718/2008 |
| 103 | Empregado - Aprendiz |
| 104 | Empregado - Doméstico |
| 105 | Empregado - Contrato a termo firmado nos termos da Lei 9.601/1998 |
| 106 | Trabalhador temporário - Contrato nos termos da Lei 6.019/1974 |
| 107 | Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS |
| 108 | Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS |
| 111 | Empregado - Contrato de trabalho intermitente |

######

#### **(2)** Tipos de IR para CR 356201

######

- **Tipo IR 14 – Rendimento PLR**

Informações de valores relacionados aos rendimentos tributáveis de Participação nos Lucros ou Resultados (PLR).

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **consolidApurMen**, na tag **vlrRendTrib**. | Consolida-se, por empresa Matriz, os rendimentos de PLR pagos aos colaboradores, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = T** – Outros tributáveis exclusivamente na fonte - **Código de incidência de IRRF = 14** |

- **Tipo IR 34 – Retenção PLR**

Informações de valores relativos ao imposto de renda retido na fonte incidente sobre PLR.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **consolidApurMen**, na tag **vlrCRMen**. | Consolida-se, por empresa Matriz, os valores de IRRF retidos sobre PLR, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = X – IRF sobre tributação exclusiva** - **Código de incidência de IRRF = 34** |

- **Tipo IR 54 – Pensão alimentícia – PLR**

Informações de valores relativos à dedução de pensão alimentícia incidente sobre rendimentos de PLR.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados exclusivamente os valores da tag **vlrDedPenAlim**, do grupo **penAlim**, quando **tpRend = 14**. | Consolida-se, por empresa Matriz, os valores de pensão alimentícia descontados sobre PLR, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = J** – Pensão Judicial - **Código de incidência de IRRF = 54** - **Identificação do Evento = 149** – Evento Pensão Alimentícia PLR |

- **Tipo IR 9014 – Exigibilidade suspensa – Rendimento tributável PLR**

Informações de valores relacionados a rendimentos de PLR com exigibilidade suspensa, decorrentes de processo administrativo ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **infoProcRet / infoValores**, na tag **vlrRendSusp**. | Consolida-se, por empresa Matriz, os rendimentos de PLR com exigibilidade suspensa, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Código de incidência de IRRF = 9014** - **Base DIRF = 6** – Tributação com exigibilidade suspensa **Número do processo** (S-5002) **= Número do processo no Sistema, com IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9034 – Exigibilidade suspensa – Retenção do IRRF PLR**

Informações de valores relacionados à retenção de IRRF sobre PLR não efetuada em razão de processo administrativo ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **infoProcRet / infoValores**, na tag **vlrNRetido**. | Consolida-se, por empresa Matriz, os valores de IRRF sobre PLR com exigibilidade suspensa, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Código de incidência de IRRF = 9034** - **Base DIRF = 6** – Tributação com exigibilidade suspensa - **Número do processo (S-5002) = Número do processo no Sistema, com IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9834 – Depósito judicial – PLR**

Informações de valores relacionados a depósito judicial de PLR em função de processo administrativo ou judicial.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **infoProcRet / infoValores**, na tag **vlrDepJud**. | Consolida-se, por empresa Matriz, os valores de PLR depositados judicialmente, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Código de incidência de IRRF = 9834** - **Base DIRF = 6** – Tributação com exigibilidade suspensa - **Identificação do Evento = 159 – Evento Depósito Judicial** - **Número do processo (S-5002) = Número do processo no Sistema, com IRRF = ‘S’** - **Evento vinculado ao processo.** |

- **Tipo IR 9054 – Exigibilidade suspensa – Dedução Pensão alimentícia – PLR**

Informações de valores relacionados à dedução de pensão alimentícia sobre PLR com exigibilidade suspensa.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **356201**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dedSusp / benefPen**, na tag **vlrDepenSusp**, quando **indTpDeducao = 5 – Pensão alimentícia**. | Consolida-se, por empresa Matriz, os valores de dedução de pensão alimentícia sobre PLR com exigibilidade suspensa, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Código de incidência de IRRF = 9054** - **Base DIRF = 6** – Tributação com exigibilidade suspensa - **Identificação do Evento = 168** – Evento de Pensão Alimentícia – PLR - **Número do processo (S-5002) = Número do processo no Sistema** - **Evento vinculado ao processo.** |

#### **(1)** CR 188901 – Rendimentos Recebidos Acumuladamente RRA

######

Este Código de Receita contempla [**todos os trabalhadores em geral**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/tabelas.html#01)**,** que tenham rendimentos de meses ou anos-calendário anteriores ao do recebimento efetivo. 

######

**(2)** **Tipos de IR para CR 188901**

- **Tipo IR 11 – Remuneração mensal**

Informações de valores relacionados aos rendimentos tributáveis pagos mensalmente, incluindo remuneração regular e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 11**. | Consolida-se, por empresa Matriz, os rendimentos tributáveis pagos aos colaboradores, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = S –** Entra como rendimento tributável - **Evento de RRA = ‘S’** - **Código de incidência de IRRF = 11 ou 13** |

- **Tipo IR 12 – 13º salário**

Informações de valores relacionados aos rendimentos do 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 12**. | Consolida-se, por empresa Matriz, os rendimentos de 13º salário pagos aos colaboradores, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = M** – 13º Salário - **Evento de RRA = ‘S’** - **Código de incidência de IRRF = 12** |

- **Tipo IR 31 – Retenção do IRRF sobre remuneração mensal**

Informações de valores relativos ao IRRF retido sobre rendimentos do trabalho, mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 31**. | Consolida-se, por empresa Matriz, os valores de IRRF retidos sobre remuneração mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = R** – IRF sobre rendimentos tributáveis - **Código de incidência de IRRF = 31 ou 33** - **Evento de RRA = ‘S’** **Identificação do Evento = 145** – IRRF RRA |

- **Tipo IR 32 – Retenção do IRRF sobre 13º salário**

Informações de valores relativos ao IRRF retido sobre rendimentos de 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 32**. | Consolida-se, por empresa Matriz, os valores de IRRF retidos sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = K –** IRF sobre rendimentos tributáveis 13º - **Código de incidência de IRRF = 32** - **Evento de RRA = ‘S’** - **Identificação do Evento = 145** – IRRF RRA |

- **Tipo IR 41 – Previdência Social Oficial (PSO) – Remuneração mensal**

Informações de valores relativos à contribuição previdenciária oficial incidente sobre remuneração mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 41**. | Consolida-se, por empresa Matriz, os valores de contribuição previdenciária oficial sobre remuneração mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = I** – Contribuição Previdenciária Oficial - **Código de incidência de IRRF = 41 ou 43** - **Evento de RRA = ‘S’** - **Identificação do Evento = 146** – INSS RRA |

- **Tipo IR 42 – Previdência Social Oficial (PSO) – 13º salário**

Informações de valores relativos à contribuição previdenciária oficial incidente sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 42**. | Consolida-se, por empresa Matriz, os valores de contribuição previdenciária oficial sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = E** – Contribuição Previdenciária Oficial 13º - **Código de incidência de IRRF = 42** - **Evento de RRA = ‘S’** - **Identificação do Evento = 146** – INSS RRA |

- **Tipo IR 46 – Previdência complementar – Remuneração mensal**

Informações de valores relativos à dedução mensal de previdência complementar.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 46**. | Consolida-se, por empresa Matriz, os valores de dedução de previdência complementar mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período informado no filtro, respeitando os critérios.   - **Base DIRF = H –** Previdência privada - **Código de incidência de IRRF = 46 ou 48** - **Identificação do Evento = 165 –** Evento de Previdência Privada – Salário mensal - **Evento de RRA = ‘S’** |

- **Tipo IR 47 – Previdência complementar – 13º salário**

Informações de valores relativos à dedução de previdência complementar incidente sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 47**. | Consolida-se, por empresa Matriz, os valores de dedução de previdência complementar sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = H –** Previdência privada - **Código de incidência de IRRF = 47** - **Identificação do Evento = 147** – Evento Previdência Privada 13º - **Evento de RRA = ‘S’** |

- **Tipo IR 61 – FAPI – Remuneração mensal**

Informações de valores relativos à dedução mensal de Fundo de Aposentadoria Programada Individual (FAPI).

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 61**. | Consolida-se, por empresa Matriz, os valores de dedução de FAPI sobre remuneração mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = 3 –** Rendimentos Tributáveis – Dedução – FAPI - **Código de incidência de IRRF = 61 ou 66** - **Identificação do Evento = 152 – Evento FAPI Remuneração Mensal** - **Evento de RRA = ‘S’** |

- **Tipo IR 62 – FAPI – 13º salário**

Informações de valores relativos à dedução de FAPI incidente sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 62**. | Consolida-se, por empresa Matriz, os valores de dedução de FAPI sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = 3 –** Rendimentos Tributáveis – Dedução – FAPI - **Código de incidência de IRRF = 62** - **Identificação do Evento = 153 –** Evento FAPI 13º - **Evento de RRA = ‘S’** |

- **Tipo IR 63 – Funpresp – Remuneração mensal**

Informações de valores relativos à dedução mensal de previdência complementar do servidor público (Funpresp).

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 63**. | Consolida-se, por empresa Matriz, os valores de dedução de Funpresp sobre remuneração mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = 4** – Rendimentos Tributáveis – Dedução – Fundo de Servidor Público - **Código de incidência de IRRF = 63 ou 65** - **Identificação do Evento = 154 –** Evento Funpresp Remuneração Mensal - **Evento de RRA = ‘S’** |

- **Tipo IR 64 – Funpresp – 13º salário**

Informações de valores relativos à dedução de Funpresp incidente sobre o 13º salário.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 64**. | Consolida-se, por empresa Matriz, os valores de dedução de Funpresp sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = 4** – Rendimentos Tributáveis – Dedução – Fundo de Servidor Público - **Código de incidência de IRRF = 64** - **Identificação do Evento = 155 –** Evento Funpresp 13º - **Evento de RRA = ‘S’** |

- **Tipo IR 51 – Pensão alimentícia – Remuneração mensal e férias**

Informações de valores relativos à dedução de pensão alimentícia incidente sobre remuneração mensal e férias.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados exclusivamente os valores da tag **vlrDedPenAlim**, do grupo **penAlim**, quando **tpRend = 18**. | Consolida-se, por empresa Matriz, os valores de pensão alimentícia descontados da remuneração mensal, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.  A apuração utiliza as datas de pagamento das tabelas **TFPFOL** e **TFPBAS**, desde que atendida a condição abaixo:   - **Base DIRF = J** – Pensão Judicial - **Evento de RRA = ‘S’** |

- **Tipo IR 70 – Parcela isenta 65 anos – Remuneração mensal**

Informações de valores relativos à parcela isenta de rendimentos pagos a beneficiários com idade igual ou superior a 65 anos.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 70**. | Consolida-se, por empresa Matriz, os valores de parcela isenta pagos mensalmente, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Código de incidência de IRRF = 70** - **Evento de RRA = ‘S’** |

- **Tipo IR 71 – Parcela isenta 65 anos – 13º salário**

Informações de valores relativos à parcela isenta aplicada ao 13º salário de beneficiários com 65 anos ou mais.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 71**. | Consolida-se, por empresa Matriz, os valores de parcela isenta pagos sobre 13º salário, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Código de incidência de IRRF = 71** - **Evento de RRA = ‘S’** |

- **Tipo IR 76 – Rendimentos por moléstia grave ou acidente – Remuneração mensal**

Informações de valores relativos a rendimentos pagos a beneficiários com moléstia grave ou acidente em serviço.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 76**. | Consolida-se, por empresa Matriz, os valores pagos a beneficiários com moléstia grave ou acidente em serviço, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = P –** Pensão, aposentadoria ou reforma por invalidez **Código de incidência de IRRF = 76** - **Identificação do Evento = 173** – Evento Moléstia Grave – Remuneração - **Evento de RRA = ‘S’** |

- **Tipo IR 77 – Rendimentos por moléstia grave ou acidente – 13º salário**

Informações de valores relativos a rendimentos de 13º salário pagos a beneficiários com moléstia grave ou acidente em serviço.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 77**. | Consolida-se, por empresa Matriz, os valores pagos sobre 13º salário a beneficiários com moléstia grave ou acidente em serviço, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = P –** Pensão, aposentadoria ou reforma por invalidez - **Código de incidência de IRRF = 77** - **Identificação do Evento = 158 –** Moléstia Grave ou Acidente – 13º - **Evento de RRA = ‘S’** |

- **Tipo IR 704 – Juros de mora**

Informações de valores relativos a juros de mora recebidos pelo atraso no pagamento de remuneração.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 704**. | Consolida-se, por empresa Matriz, os valores pagos a título de juros de mora, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - **Base DIRF = C –** Informações complementares - **Código de incidência de IRRF = 704** - **Evento de RRA = ‘S’** |

- **Tipo IR 7900 – Verbas de natureza diversa**

Informações de valores transitados pela folha que não representam rendimento, retenção, isenção ou dedução de IR.

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Consolida os valores do evento S-5002, considerando o Código de Receita (CR) **188901**, agrupados por empresa Matriz e dentro do período de apuração selecionado (mensal ou anual).  São considerados os valores do grupo **dmDev / totApurMen**, filtrando os registros com **CRMen = 188901** e **tpInfoIR = 7900**. | Consolida-se, por empresa Matriz, os valores de verbas não tributáveis transitadas pela folha, considerando exclusivamente pagamentos cuja data esteja dentro do período filtro, respeitando os critérios.   - Exceto eventos com **Natureza da Rubrica = 9219 (Plano de saúde)** - **Código de incidência de IRRF = 09** - **Evento de RRA = ‘S’** |

######

#### **(1)** CR - 061001- IRRF sobre rendimentos relativos a prestação de serviços de transporte rodoviário internacional de carga, pagos a transportador autônomo PF residente no Paraguai

######

Este Código de Receita contempla **todos trabalhadores** com **categoria 712 -** Contribuinte individual - Transportador autônomo de carga residentes no exterior **país 586 - Paraguai.**

Para cada **tipo de IR** será seguido o seguinte:

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Para cada Tipo de IR, o valor apresentado é apurado a partir do retorno do evento **S-5002**, utilizando as **mesmas tags e grupos** aplicáveis aos Tipos de IR do **CR 056107**.  A diferença é que, para o **CR 061001**, a consolidação considera **exclusivamente os trabalhadores** que atendam aos critérios específicos definidos para esse **Código de Receita**. | O valor apurado pelo Sistema para cada **Tipo de IR** segue os **mesmos critérios de configuração de eventos** já estabelecidos para os demais Códigos de Receita.  Neste caso, a consolidação considera **somente os trabalhadores** cujos eventos atendam integralmente aos critérios definidos para o **CR 061001**. |

######

#### **(1)**CR 056111 - IRRF - Empregado/Trabalhador rural Segurado especial

######

Este Código de Receita contempla **trabalhador segurado especial e empregador doméstic**o com recolhimento unificado.

- **Categorias de trabalhadores consideradas para CR 056111**

Desde que a **classificação tributária** do **empregador** seja **igual à 22** (Segurado especial, inclusive quando for empregador doméstico).

| **Categoria dos Trabalhadores** | |
| --- | --- |
| 101 | Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT |
| 102 | Empregado - Trabalhador rural por pequeno prazo da Lei 11.718/2008 |
| 103 | Empregado - Aprendiz |
| 105 | Empregado - Contrato a termo firmado nos termos da Lei 9.601/1998 |
| 106 | Trabalhador temporário - Contrato nos termos da Lei 6.019/1974 |
| 107 | Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS |
| 108 | Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS |
| 111 | Empregado - Contrato de trabalho intermitente |

Para cada **tipo de IR** será seguido o seguinte:

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Para cada Tipo de IR, o valor apresentado é apurado a partir do retorno do evento **S-5002**, utilizando as **mesmas tags e grupos** aplicáveis aos **Tipos de IR** do **CR 056107**.  A diferença é que, para o **CR 056111**, a consolidação considera **exclusivamente os trabalhadores** que atendam aos critérios específicos definidos para esse **Código de Receita**. | O valor apurado pelo Sistema para cada **Tipo de IR** segue os **mesmos critérios de configuração de eventos** já estabelecidos para os demais Códigos de Receita.  Neste caso, a consolidação considera **somente os trabalhadores** cujos eventos atendam integralmente aos critérios definidos para o **CR 056111**. |

######

#### **(1)** CR 056112 - IRRF - Empregado/Trabalhador rural Segurado especial 13° salário

######

Este Código de Receita contempla **trabalhador segurado especial e empregador doméstic**o com recolhimento unificado apenas para **13° salário,** com **exceção** dos valores **originados** dos envios dos **S-2299/S-2399.**

- **Categorias de trabalhadores consideradas para CR 056112**

Desde que a **classificação tributária** do **empregador** seja **igual à 22** (Segurado especial, inclusive quando for empregador doméstico) de origem **13° salário.**

| **Categoria dos Trabalhadores** | |
| --- | --- |
| 101 | Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT |
| 102 | Empregado - Trabalhador rural por pequeno prazo da Lei 11.718/2008 |
| 103 | Empregado - Aprendiz |
| 105 | Empregado - Contrato a termo firmado nos termos da Lei 9.601/1998 |
| 106 | Trabalhador temporário - Contrato nos termos da Lei 6.019/1974 |
| 107 | Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS |
| 108 | Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS |
| 111 | Empregado - Contrato de trabalho intermitente |

Para cada **tipo de IR** será seguido o seguinte:

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Para cada Tipo de IR, o valor apresentado é apurado a partir do retorno do evento **S-5002**, utilizando as **mesmas tags e grupos** aplicáveis aos **Tipos de IR** do **CR 056107**.  A diferença é que, para o **CR 056112**, a consolidação considera **exclusivamente os trabalhadores** que atendam aos critérios específicos definidos para esse **Código de Receita**. | O valor apurado pelo Sistema para cada **Tipo de IR** segue os **mesmos critérios de configuração de eventos** já estabelecidos para os demais Códigos de Receita.  Neste caso, a consolidação considera **somente os trabalhadores** cujos eventos atendam integralmente aos critérios definidos para o **CR 056112**. |

######

#### **(1)** CR 056113 - IRRF - Empregado/Trabalhador rural Segurado especial 13° salário

######

Este Código de Receita contempla **trabalhador segurado especial e empregador doméstic**o com recolhimento unificado apenas para **13° salário,** que **seja apenas** valores **originados** dos envios dos **S-2299/S-2399.**

- **Categorias de trabalhadores consideradas para CR 056113**

Desde que a **classificação tributária** do **empregador** seja **igual à 22** (Segurado especial, inclusive quando for empregador doméstico) de origem **13° salário, originados** dos envios dos **S-2299/S-2399.**

| **Categoria dos Trabalhadores** | |
| --- | --- |
| 101 | Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT |
| 102 | Empregado - Trabalhador rural por pequeno prazo da Lei 11.718/2008 |
| 103 | Empregado - Aprendiz |
| 105 | Empregado - Contrato a termo firmado nos termos da Lei 9.601/1998 |
| 106 | Trabalhador temporário - Contrato nos termos da Lei 6.019/1974 |
| 107 | Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS |
| 108 | Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS |
| 111 | Empregado - Contrato de trabalho intermitente |

Para cada **tipo de IR** será seguido o seguinte:

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Para cada Tipo de IR, o valor apresentado é apurado a partir do retorno do evento **S-5002**, utilizando as **mesmas tags e grupos** aplicáveis aos **Tipos de IR** do **CR 056107**.  A diferença é que, para o **CR 056113**, a consolidação considera **exclusivamente os trabalhadores** que atendam aos critérios específicos definidos para esse **Código de Receita**. | O valor apurado pelo Sistema para cada **Tipo de IR** segue os **mesmos critérios de configuração de eventos** já estabelecidos para os demais Códigos de Receita.  Neste caso, a consolidação considera **somente os trabalhadores** cujos eventos atendam integralmente aos critérios definidos para o **CR 056113**. |

######

#### **(1)** CR 047301– IRRF – Residentes no exterior, para fins fiscais

######

Este Código de Receita contempla **todos os trabalhadores residentes no exterior para fins fiscais,**  ou seja que atenda o critério abaixo:

Funcionário com categoria diferente de **( ≠ ) 712** - Contribuinte individual - Transportador autônomo de carga e que seja residente no exterior e tenha qualquer código de país informado de acordo com a [Tabela 06 - Países](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/tabelas.html#06).

Funcionário com categoria igual **( =) 712** - Contribuinte individual - Transportador autônomo de carga e que seja residente no exterior e tenha código do país informado diferente de 586 - Paraguai.

Para cada **tipo de IR** será seguido o seguinte:

| **Valor eSocial** | **Valor Sistema** |
| --- | --- |
| Para cada Tipo de IR, o valor apresentado é apurado a partir do retorno do evento **S-5002**, considerando exclusivamente as informações das tags **vlrPagoDia** e **vlrCRDia**, localizadas no grupo **totApurDia**.  A consolidação dos valores respeita o enquadramento do Tipo de IR e o **Código de Receita (CR) 047301**, conforme retorno do eSocial. | O valor apurado pelo Sistema segue os **mesmos critérios de configuração de eventos** já descritos para os demais Códigos de Receita.  A diferença neste caso é que a consolidação considera **somente os trabalhadores cujos atendam integralmente aos critérios definidos para o CR 047301**. |

######

### 4. Pontos de Atenção

- Divergências nem sempre indicam erro: podem ser diferença de **período**, **retificação** ou **configuração**.
- Eventos com incidência ou base DIRF incorreta impactam diretamente os valores.
- Processos judiciais exigem:

  - Número do processo informado;
  - Evento vinculado corretamente;
  - Incidência e base DIRF compatíveis.

######

### 5. Dicas de Usabilidade

- Sempre valide o **período de apuração** antes de analisar diferenças.
- Use o **segundo nível do dashboard** para identificar a origem exata da divergência.
- Compare os valores com o **extrator da Receita Federal**.
- Em casos de exigibilidade suspensa, confira:

  - Processo judicial;
  - Abrangência;
  - Tipo de INSS;
  - Identificação do evento.
- Utilize a exportação para Excel em análises com grande volume de dados.

######

## Artigos Relacionados

######

[Nova DIRF/eSocial 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361211258647)

[Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071)

[Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231-Relat%C3%B3rio-S-5012-IRRF-consolidado-por-contribuinte#top)
