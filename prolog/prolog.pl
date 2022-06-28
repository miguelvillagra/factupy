
% Autor: Miguel Villagra / miguel.villagra@fpuna.edu.py

% Tipo de productos a la venta.

pastel('pastel_gourmet').
pastel('pastel_helado').
pastel('pastel_pequeno').
pastel('pastel_mediano').

pastel_economico('pastel_pequeno').
pastel_economico('pastel_mediano').

% Regla.
producto_a_la_venta(X):- pastel(X).
pastel_no_economico(X):- pastel(X),  not(pastel_economico(X)).
