<?php

namespace App\Http\Controllers;

use App\Book;
use App\LendingRecord;
use App\User;
use Auth;
use Illuminate\Http\Request;

class BooksController extends Controller
{
    /**
     * Only user can add a book
     */
    public function __construct()
    {

        $this->middleware('auth')->only(['store']);
    }

    /**
     *
     * Show all the books
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function index()
    {
        $items = Book::orderBy('created_at','desc')->paginate(20);

        return view('books.index',compact('items'));
    }

    /**
     * Show all the books through api
     *
     * @return mixed
     */
    public function apiIndex()
    {
        $items = Book::orderBy('created_at','desc')->paginate(20);

        return $items;
    }

    /**
     * User create a book
     */
    public function store()
    {
        Auth::user()->books()->create(request(['name','detail']));

        return back();

    }


    /**
     *
     * User's books
     *
     * @param $user_id
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function userBooks($user_id)
    {
        $user_name = User::find($user_id)->name;

        $items = Book::where('user_id',$user_id)->orderBy('created_at','desc')->paginate(20);

        return view('books.userIndex',compact('items','user_name'));
    }

    public function bookDetail($book_id)
    {

        $book = Book::find($book_id);

        $items = LendingRecord::where('book_id',$book_id)->orderBy('start_at','desc')->paginate(20);

        return view('books.book',compact('items','book'));
    }
}
