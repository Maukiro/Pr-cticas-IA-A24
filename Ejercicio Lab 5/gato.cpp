#include <iostream>
#include <vector>
#include <time.h>
#include <algorithm>
#include <stdlib.h>
#include <map>
#define MOD 1000000007
using namespace std;
typedef long long int ll;
struct RNG{
    ll semilla;
    ll azar(){
        semilla*=semilla;
        semilla%=MOD;
        semilla+=rand()%9999999;
        semilla*=semilla;
        semilla%=MOD;
        return semilla;
    }
}generator;
struct nodo;
struct descicion{
    nodo *direccion;
    int desenlace;
    int jugada;
    //descicion(nodo * dir,int valor,int pos):direccion(dir),desenlace(valor),jugada(pos){};
};
bool prioprimero(descicion a, descicion b){
    if(a.desenlace == 1 && b.desenlace!=1)return true;
    if(a.desenlace!=1 && b.desenlace==1)return false;
    if(a.desenlace ==-1 && b.desenlace==2) return true;
    if(a.desenlace ==2 && b.desenlace == -1)return false;
    return true;
}
bool priosegundo(descicion a, descicion b){
    if(a.desenlace == 2 && b.desenlace!=2)return true;
    if(a.desenlace!=2 && b.desenlace==2)return false;
    if(a.desenlace ==-1 && b.desenlace==1) return true;
    if(a.desenlace ==1 && b.desenlace == -1)return false;
    return true;
}
struct nodo{
    nodo *camino;
    int semilla;
    vector<nodo *> hijos;
    vector<descicion> objetivos;
    nodo():hijos(vector<nodo *>(9,nullptr)),objetivos({}),semilla(0){};
};

struct gato{
    vector<vector<int> > matrix;
    int tamano;
    bool turno;
    vector<bool> bot;
    bool termino;
    bool ganador;
    int libres;
    void imprime(){
        for(int i=0;i<tamano;i++){
            for(int j=0;j<tamano;j++){
                cout<<matrix[i][j];
            }
            cout<<"\n";
        }
    }
    void evalua(int y, int x){
        if(matrix[0][x]==matrix[1][x] && matrix[2][x] == matrix[1][x]){
            termino =1;
        }
        if(matrix[y][0]==matrix[y][1] && matrix[y][2] == matrix[y][1]){
            termino =1;
        }
        if(y == x){
            if(matrix[0][0] == matrix[1][1] && matrix[2][2]==matrix[1][1]){
                termino = 1;
            }
        }
        if(x+y == 2){
            if(matrix[0][2] == matrix[1][1] && matrix[2][0]==matrix[1][1]){
                termino = 1;
            }
        }
    }

    void azar(){
        int x;
        x = generator.azar();
        x%=libres;
        x++;
        int xpos,ypos;
        xpos=ypos=0;
        while(x>0){
            //cout<<"{"<<xpos<<","<<ypos<<"}";
            if(!matrix[ypos][xpos]){
                x--;
                //cout<<x<<",";
                if(x==0){
                    matrix[ypos][xpos] =(int)turno+1;
                    cout<<xpos+1<<","<<ypos+1<<"\n";
                    this->evalua(ypos,xpos);
                    return;
                }
            }
            xpos++;
            if(xpos==tamano){
                xpos=0;
                ypos = (ypos+1)%tamano;
            }
        }
    }

    pair<int,int> tirada(){
        int x,y;
        bool bandera = 0;
        while(!bandera){
            cin>>x>>y;
            x--;
            y--;
            if(x<0 || x>=tamano || y<0 || y>=tamano){
                cout<<"Error: No puedes colocar cosas fuera de la matriz\n";
            }else if(matrix[y][x]){
                cout<<"Error: No puedes colocar algo en una casilla ocupada\n";
            }else{
                matrix[y][x]=(int)(turno)+1;
                this->evalua(y,x);
                bandera = 1;
                return {y,x};
            }
        }
    }

    int bueno(nodo *actualNodo){
        /*for(auto z:actualNodo->objetivos){
            cout<<z.jugada<<"::"<<z.desenlace<<","<<z.direccion->semilla<<"\n"; 
        }*/
        int w = actualNodo->objetivos[0].jugada;
        matrix[w/3][w%3]=(int)(turno)+1;
        this->evalua(w/3,w%3);
        return w;
    }

    void juego(nodo *actualNodo){
        while(!termino && libres>0){
            cout<<"Turno del jugador "<<(int)(turno+1)<<((bot[turno])?"(BOT):":":")<<"\n";
            this->imprime();
            if(bot[turno]){
                int tiradaBot = this->bueno(actualNodo);
                actualNodo = actualNodo->hijos[tiradaBot];
            }else{
                if(actualNodo == nullptr){
                    cout<<"AY\n";
                }
                /*for(auto z:actualNodo->objetivos){
                    cout<<z.jugada<<"::"<<z.desenlace<<","<<z.direccion->semilla<<"\n";
                }*/
                pair<int,int> obtenido = this->tirada();
                int w = obtenido.first*3+obtenido.second;
                actualNodo = actualNodo->hijos[w];
            }
            if(termino){
                this->imprime();
                if(turno==0){
                    cout<<"Jugador 1 Gana\n";
                }else{
                    cout<<"Jugador 2 Gana\n";
                }
            }
            turno = !turno;
            libres--;
        }
        if(!termino){
            this->imprime();
            cout<<"EMPATE\n";
        }
    }
    gato(int n,bool uno,bool dos):libres(n*n),termino(0),turno(0),matrix(n+2,vector<int>(n+2)),tamano(n),bot({uno,dos}){};
};

int expbin(int base,int exponente){
    if(exponente==0)return 1;
    int resp = expbin(base,exponente/2);
    resp*=resp;
    if((exponente & 1)){
        resp*=base;
    }
    return resp;
}

void basea(int semilla, vector<vector<int> > &rep,int pos){
    if(semilla==0)return;
    basea(semilla/3,rep,pos-1);
    rep[pos/3][pos%3] = semilla%3;
}

int evalua(int semilla,int normal){
    vector<vector<int> > representacion(3,vector<int> (3));
    basea(semilla,representacion,8);
    
    for(int i=0;i<3;i++){
        if(representacion[i][0]==representacion[i][1] && representacion[i][2]==representacion[i][1] && representacion[i][0]!=0){
            return representacion[i][0];
        }
        if(representacion[0][i]==representacion[1][i] && representacion[2][i]==representacion[1][i] && representacion[0][i]!=0){
            return representacion[0][i];
        }
    }
    if(representacion[1][1]!=0){
        if((representacion[0][0]==representacion[1][1] && representacion[2][2]==representacion[1][1] )||
            (representacion[2][0] ==representacion[1][1] && representacion[0][2]==representacion[1][1]))
            return representacion[1][1];
    }
    int usadas = 0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(representacion[i][j]!=0)usadas++;
        }
    }
    return usadas==9?-1:0;
}

/*void escribecasoActual(int semilla,vector<vector<int> > &rep, int pos){
    if(semilla==0)return;
    basea(semilla/3,rep,pos-1);
    rep[pos/3][pos%3] = semilla%3;
}*/
int genera(int semilla,int normal,nodo *arbol,map<int,nodo *> & conexiones,int color,map<int,int> &dp){
    //0 indeciso, -1 empate, 1 j1 gana, 2 j2 gana
    //cout<<"Valor:\n";
    //vector<vector<int> > repDebug(3,vector<int> (3));
    //escribecasoActual(semilla,repDebug,8);
    /*for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout<<repDebug[i][j];
        }
        cout<<"\n";
    }
    cout<<"\n";*/
    int v = evalua(semilla,normal);
    //cout<<v;
    if(v!=0){
        dp[semilla] = v;
        return v;
    }
    for(int i=0;i<9;i++){
        if(((normal) & (1<<i)))continue;
        int aux = ((normal)|(1<<i));
        int nuevadir=semilla + color*expbin(3,i);
        //cout<<nuevadir<<",";
        if(!conexiones.count(nuevadir)){
            nodo *nuevo = new nodo();
            conexiones[nuevadir] = nuevo;
            arbol->hijos[i] = nuevo;
            nuevo->semilla = nuevadir;
            //cout<<"@";
        }else{
            arbol->hijos[i] = conexiones[nuevadir];
        }
        if(!dp.count(nuevadir))
            dp[nuevadir] = genera(nuevadir,aux,conexiones[nuevadir],conexiones,color%2+1,dp);
        arbol->objetivos.push_back({conexiones[nuevadir],dp[nuevadir],i});
    }
    if(color==1){
        sort(arbol->objetivos.begin(),arbol->objetivos.end(),prioprimero);
        /*cout<<"Color 1: ";
        for(auto z:arbol->objetivos){
            cout<<z.desenlace<<",";
        }
        cout<<"\n";*/
        v = arbol->objetivos[0].desenlace;
    }else{
        sort(arbol->objetivos.begin(),arbol->objetivos.end(),priosegundo);
        /*cout<<"Color 2: ";
        for(auto z:arbol->objetivos){
            cout<<z.desenlace<<",";
        }
        cout<<"\n";*/
        v = arbol->objetivos[0].desenlace;
    }
    dp[semilla] = v;
    return v;
}
void dfs(nodo *actual){
    cout<<actual->semilla<<":  ";
    for(int i=0;i<9;i++){
        if(actual->hijos[i]==nullptr){
            cout<<"-1,";
            continue;
        }
        cout<<actual->hijos[i]->semilla<<",";
    }
    cout<<"\n";
    for(int i=0;i<9;i++){
        if(actual->hijos[i]==nullptr)continue;
        dfs(actual->hijos[i]);
    }
}
int main(){
    nodo *arbol = new nodo;
    map<int,nodo *> conexiones;
    map<int,int> dp;
    conexiones[0] = arbol;
    genera(0,0,arbol,conexiones,1,dp);
    //dfs(arbol);
    //return 0;
    /*cout<<";)\n";
    cout<<conexiones.size();
    return 0;*/
    srand(time(NULL));
    bool jugador1;
    bool jugador2;
    cin>>jugador1>>jugador2;
    gato juego(3,jugador1,jugador2);
    juego.juego(arbol);
}