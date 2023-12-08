#include <iostream>

class Jaaj{
    public:
        Jaaj::Jaaj(int vie);
    private:
        int m_vie;
};

Jaaj::Jaaj(int vie) : m_vie(vie){
    std::cout << "Lesssss goooo" << std::endl;
}