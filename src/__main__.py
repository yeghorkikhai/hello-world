from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def write(self):
        ...


class Hello(Base):

    def write(self) -> bool:
        print('Hello world!')
        return True


def main():
    hello = Hello()
    hello.write()


if __name__ == '__main__':
    main()
