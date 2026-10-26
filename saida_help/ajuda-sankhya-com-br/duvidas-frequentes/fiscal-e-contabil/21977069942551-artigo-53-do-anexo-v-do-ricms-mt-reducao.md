---
id: "21977069942551"
titulo: "Artigo 53 do Anexo V do RICMS/MT - Redução Base de Cálculo 41,17% (Mato Grosso)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21977069942551-Artigo-53-do-Anexo-V-do-RICMS-MT-Redu%C3%A7%C3%A3o-Base-de-C%C3%A1lculo-41-17-Mato-Grosso"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:49:37Z"
rotulos: ["Alíquotas", "Configuração", "ICMS", "Impostos", "Mato Grosso"]
---

# Artigo 53 do Anexo V do RICMS/MT - Redução Base de Cálculo 41,17% (Mato Grosso)

Como proceder para configurar o sistema de modo a aplicar a redução da base de cálculo de 41,17% para o Estado de Mato Grosso.

#### Procedimento

Para garantir o correto funcionamento referente à Redução da Base de Cálculo de 41,17% (Mato Grosso), é imprescindível que exista uma regra de alíquota de ICMS devidamente configurada, conforme o exemplo a seguir:

**Exemplo:** 
Regra 2296 - ES x MT, configurada da seguinte maneira:

Aba Geral:

Tributação: 00
Alíquota: 12
 
Aba Substituição Tributária:

Margem de Lucro (MVA): 53,86 
Margem de Lucro (MVA) para origem estrangeira: 53,86 
Alíquota de Substituição Tributária: 17
Redução da Base ST: 58,83 (Neste campo, 100% - 58,83% = 41,17%. Portanto, ao invés de inserir 41,17%, deve-se informar 58,83% para que o cálculo seja realizado corretamente, conforme a fórmula implementada.) 
Modalidade BC ICMS ST: Margem de Valor Agregado (%)
Alíquota de ICMS Específica para o cálculo de ST: 7 
Tipo de Cálculo de ST Específico: 13 - Realizar o cálculo de ICMS para redução na ST com alíquota específica e utilizando o mesmo percentual de redução do ST
 
Fórmula do Cálculo Específico, conforme o HELP:

 
![Imagem 1: Margem de Lucro (MVA): 53,86 Margem de Lucro (MVA) para origem estrangeira: 53,86 Alíquota de Substituição Tributária:…](https://ajuda.sankhya.com.br/attachments/token/ZrCpvSEUvFAOLwT5trTJUQVzT/?name=image.png)

![Imagem 2: Margem de Lucro (MVA): 53,86 Margem de Lucro (MVA) para origem estrangeira: 53,86 Alíquota de Substituição Tributária:…](https://ajuda.sankhya.com.br/hc/article_attachments/21977390547735)
