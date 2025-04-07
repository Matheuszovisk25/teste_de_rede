import streamlit as st
import pandas as pd

st.title("Instabilidade de Rede")

st.write("""No dia 04/04/2025, foi identificada uma instabilidade na rede que teve início durante o período do almoço. A situação se agravou ao longo do dia, resultando em queda total da conexão com a internet às 16h20.

A seguir, apresento o passo a passo detalhado dos testes realizados e das ações tomadas na tentativa de diagnosticar e solucionar o problema. """)

with st.expander("Primeiro teste - Verificação da Conectividade no Mikrotik da Vega"):
    st.write("O primeiro teste foi realizado diretamente no roteador Mikrotik da Vega IT, com o objetivo de verificar se o link de internet estava ativo e funcional.")
    st.image("images2/vega_mickotik.jpeg")
    st.image("images2/teste_mickotic_vega.jpeg")
    st.write("""Resultado:
Foi constatado que o sistema da Vega IT estava recebendo sinal de internet, porém não conseguia distribuir corretamente a conexão. Mesmo com a conexão direta ao link da Vega, nenhum site ou serviço era carregado, indicando uma falha na distribuição do sinal ou possível problema no MickoTik.""")
    
with st.expander("Segundo teste - Teste de Conectividade no Roteador da TrixNet"):
    st.write("O segundo teste foi realizado no roteador da TrixNet. A conexão foi feita diretamente pelo cabo de rede, sem passar por nenhum outro equipamento intermediário.")
    st.image("images2/aparelho_trix_net1.jpeg")
    st.image("images2/teste_trix_net.jpeg")
    st.write("""Resultado:
             Foi confirmado que o roteador da TrixNet estava recebendo internet normalmente. Durante o teste, todos os sites e serviços acessados funcionaram corretamente, incluindo portais de notícias, YouTube e outros aplicativos online, o que indicou que o link da operadora estava estável e funcionando como esperado.""")
    
with st.expander("Terceiro teste - Verificação do Roteador da Claro"):
    st.write("O terceiro teste foi realizado no roteador da Claro, outro ponto de entrada de internet na rede local.")
    st.image("images2/claro_aparelho.jpeg")
    st.write("""Resultado:
Assim como no teste anterior, foi constatado que o roteador da Claro estava funcionando normalmente, com conexão estável e acesso completo à internet. Sites, serviços e plataformas online responderam sem problemas, o que reforça que o problema não estava relacionado aos provedores ou ao sinal de internet recebido""")
    
with st.expander("Quarto teste - Segundo roteador Trixnet"):
    st.write("O quarto teste foi realizado em um segundo equipamento da TrixNet.")
    st.image("images2/segundo_roteador_trix.jpeg")
    st.write("""Resultado:
Foi constatado que esse segundo aparelho da TrixNet não estava fornecendo internet, mesmo com conexão direta via cabo. Nenhum site ou serviço online foi carregado. """)


st.title("Contato com a Operadora TrixNet")

st.write("""Ainda no dia 04/04/2025, entramos em contato com o suporte técnico da TrixNet para relatar a instabilidade. A operadora informou um prazo de até 24 horas para atendimento, mas retornou o contato às 08h00 da manhã do dia seguinte.

Durante o atendimento, solicitamos a remoção da configuração em modo bridge do equipamento, e em seguida desligamos os aparelhos da Vega IT para testar a conexão da TrixNet de forma isolada.

Com os equipamentos da Vega desligados e a remoção do bridge, a internet passou a funcionar normalmente, confirmando que o link da TrixNet estava operando corretamente.

Para restabelecer o funcionamento da rede interna e permitir que os colaboradores voltassem a trabalhar, foi realizada a alteração do IP do roteador, configurando-o para atuar na mesma faixa de IP do IP administrativo (IP ADM). A partir dessa mudança, os dispositivos voltaram a ter acesso à internet.""")

st.title("Conclusão")

st.write("""Após a realização dos testes, foi possível concluir que o problema de instabilidade e queda de internet ocorrido no dia 04/04/2025 não estava relacionado à falha no fornecimento de internet pelas operadoras TrixNet ou Claro, uma vez que ambas apresentaram conectividade normal em seus respectivos roteadores.

O problema se concentrou no roteador Mikrotik da Vega IT, que apesar de receber sinal de internet, não conseguia distribuí-lo corretamente para os demais dispositivos da rede. Isso indica uma possível falha de configuração, saturação do equipamento ou problema interno no roteador, sendo esse o principal ponto a ser investigado para evitar recorrência da falha.""")