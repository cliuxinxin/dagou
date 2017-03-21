<?php

namespace App\Http\Controllers;

use App\Book;
use App\LendingRecord;
use Auth;
use Carbon\Carbon;
use Illuminate\Http\Request;

class LendingRecordsController extends Controller
{
    /**
     * Only user can lend a book
     */
    public function __construct()
    {

        $this->middleware('auth')->only(['store']);
    }

    /**
     *
     * Generate a record update book status
     *
     * @param Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function store(Request $request)
    {
        $book_id = $request->book_id;

        Book::find($book_id)->update([
            'is_lended' => 'Y'
        ]);

        Auth::user()->lendingRecords()->create([
            'book_id' => $book_id,
            'start_at' => Carbon::now()
        ]);

        return back();
    }

    public function update(Request $request)
    {
        $book_id = $request->book_id;
        $lending_record_id = $request->lending_record_id;

        Book::find($book_id)->update([
            'is_lended' => 'N'
        ]);

        LendingRecord::find($lending_record_id)->update([
            'end_at' => Carbon::now()
        ]);

        return back();
    }
}
