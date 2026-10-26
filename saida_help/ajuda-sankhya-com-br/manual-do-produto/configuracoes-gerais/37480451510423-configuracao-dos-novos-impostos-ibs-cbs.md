---
id: "37480451510423"
titulo: "Configuração dos novos impostos (IBS, CBS) para uso no Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37480451510423-Configura%C3%A7%C3%A3o-dos-novos-impostos-IBS-CBS-para-uso-no-Fast-Service"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Configurações gerais"
atualizado_em: "2026-07-29T22:13:41Z"
rotulos: ["Configuração", "Fast Service", "Atualização", "Impostos", "Reforma Tributária", "Fast Service e reforma tributária", "Impostos reforma tributária", "Configuração dos novos impostos (IBS CBS) para uso no Fast Service", "Impostos reforma tributária no Fast Service", "IBS e CBS no Fast Service", "SankhyaOm"]
---

# Configuração dos novos impostos (IBS, CBS) para uso no Fast Service

A partir da ativação da **“Nota Técnica 2025.002-RTC – v1.10”** e com a TOP configurada para calcular algum imposto da Reforma Tributária ([Guia rápido: prepare seu sistema para a Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/34971966800151-Guia-r%C3%A1pido-prepare-seu-sistema-para-a-Reforma-Tribut%C3%A1ria)), o Fast Service passará a exigir conexão com o SankhyaOM para o cálculo desses impostos.
 
Para que o Fast Service se comunique corretamente com o SankhyaOM, é necessário que:

- O parâmetro **URLSANKHYAW** esteja configurado com o endereço do **SankhyaOM**;
- O SanNFe esteja atualizado para a última versão disponível (**versão publicada em 26/12/2025 ou superior**);
- O SankhyaOM esteja atualizado para a versão **4.35b424** ou superior;
- A versão do **FAST** seja **4.66.0.35** ou superiores (disponível no place.sankhya.combr >> Downloads >> Executáveis, "MGE - Emissor de Cupom Fiscal").

**ATENÇÃO:**

Vale destacar que o **Fast Service** não terá mais a possibilidade de funcionamento offline (sem conexão com o SankhyaOM), uma vez que o cálculo dos novos impostos e a geração do XML passarão a ser realizados diretamente pelo ERP.

Essa funcionalidade foi disponibilizada apenas como apoio durante o processo de migração definitiva para o SankhyaOM. Não serão feitas melhorias nem adequações posteriores, uma vez que o Sunset ainda ocorrerá de acordo com a programação.
