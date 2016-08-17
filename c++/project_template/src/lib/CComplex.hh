/*****************************************************************************
 * File:  CComplex
 *
 * Description: Example class for setting some content in the project
 *
 *
 *
 * *****************************************************************************/ 



#ifndef __CCOMPLEX_HH__
#define __CCOMPLEX_HH__

#include <ostream>
#include <istream>


template <typename T> 
class CComplex {
    private:
        T _real;
        T _img;

        // Prevent copying 
        CComplex(const CComplex&); 
        //CComplex& operator=(const CComplex&); 

    public:
        CComplex(T r, T i) :
            _real(r),
            _img(i) {


            };


		CComplex<T>& operator+=(const CComplex<T>& r) {                      
                this._real += r._real;
                this._img  += r._img;
				
				return *this; 
		}

		friend CComplex<T>& operator+(CComplex<T>& l, const CComplex<T>& r) {
			l._real += r._real; 
			l._img  += r._img; 
			return l; 
		}


        T& getReal() { return _real; };
        T& getImg()  { return _img;  };


};
template <typename T> 
std::ostream& operator<<(std::ostream& os, const CComplex<T>& o)
{
    return os;
}

template <typename T> 
std::istream& operator>>(std::istream& is, CComplex<T>& o)
{
    return is;
}



template <typename T> 
inline bool operator< (const CComplex<T>& l, const CComplex<T>& r){ 
	bool result; 

	if (l._real == r._real)  {
		result = l._img < r._img;
	} else {
		result =  l._real < r._real;
	}

    return result;

}

template <typename T> 
inline bool operator> (const CComplex<T>& l, const CComplex<T>& r) {return r< l;    }

template <typename T> 
inline bool operator<=(const CComplex<T>& l, const CComplex<T>& r) {return !(l> r); }

template <typename T> 
inline bool operator>=(const CComplex<T>& l, const CComplex<T>& r) {return !(l< r); }

template <typename T> 
inline bool operator==(const  CComplex<T>& l, const CComplex<T>& r) { 
  return (l._real == r._real)  and ( l._img  == r._img);
}

template <typename T> 
inline bool operator!=(const CComplex<T>& l, const CComplex<T>& r) {return !(l== r);}


#endif
