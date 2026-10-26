---
id: "360044579934"
titulo: "Melhores Práticas para Emissão do 'CT-e Globalizado'."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579934-Melhores-Pr%C3%A1ticas-para-Emiss%C3%A3o-do-CT-e-Globalizado"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:24Z"
rotulos: ["DUVIDACTE", "CT-e", "CT-e Globalizado", "Configuração", "XML", "Transporte", "CFOP", "Transporta várias NF-e dentro do estado", "TOP com tipo de movimento \"Venda\" CFOP 5932", "Marque 'CT-e Globalizado' adicione 5 NF-e's e verifique tag XML", "Documentos Eletrônicos"]
---

# Melhores Práticas para Emissão do 'CT-e Globalizado'.

Utilizado para acobertar várias operações de transporte em uma mesma CT-e, seja de envio de mercadoria, quanto de coleta de mercadoria.

- O transporte ocorre exclusivamente apenas dentro do estado.
- O CT-e deve ter como tomador apenas o remetente ou o destinatário.
- Deve haver o vinculo de no minimo 5(cinco) NF-e's de CNPJs diferentes.
- A razão social do Destinatário ou Remetente, conterá a literal "DIVERSOS" no XML e Impressão.

**Configuração e Lançamento de CT-e Globalizado**

Configurações da TOP de CT-e Normal
Tipo de Movimento: V-Venda
Atualização de Livro ICMS = Livro de Saida
CT-e: Normal
Tipo de Serviço CT-e: Normal
Tipo de Emissão CT-e: Normal

CFOPs:
DENTRO do estado = CFOP 5932
Fora do Estado = CFOP 6932

Comercial » Rotinas » Central de Vendas >>Conhecimento de Transporte

Ao lançar o cabeçalho da CT-e, marque a opçao 'CT-e Globalizado'

No 'Rodapé', importe ou lance manual as 5 chaves das NF-e's, aba: Notas do Conhecimento de Transporte.

No XML, terá a tag, sinalizando que é um CT-e Globalizado.

<ide>

...

<indGlobalizado>1</indGlobalizado>

...

</ide>

E a informação das 5 NF-e que compõem a CT-e.

<infDoc>
 <infNFe>
 <chave>31171026314062000161550010000334981920966854</chave>
 </infNFe>
 <infNFe>
 <chave>35170907222536000109550010003412931155748251</chave>
 </infNFe>
 <infNFe>
 <chave>53170626314062000757550010000422451082661012</chave>
 </infNFe>
 <infNFe>
 <chave>35160610276926000249550010000332641983892423</chave>
 </infNFe>
 <infNFe>
 <chave>51160218907178000186550010000110114393167849</chave>
 </infNFe>
 </infDoc>

**Observação:**

Manual do Contribuinte CT-e:
<http://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=YIi+H8VETH0=>
